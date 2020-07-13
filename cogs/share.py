import discord 
import asyncio
import random
from discord.ext import commands
import os
import datetime
import pymongo
import json
import math

db_client=pymongo.MongoClient(os.getenv("DB_URL"))
db1_client=pymongo.MongoClient(os.getenv("DB2_URL"))
db_name=db1_client["Challenge"]
db_collection=db_name['Data']
db1_name=db1_client['Running_matches']
db1_collection=db1_name['data']
db2_name=db_client["about"]
db2_collection=db2_name["data"]
class share(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @commands.command(aliases=["give","transfer"])
    @commands.guild_only()
    async def share(self,ctx,trainer2: discord.Member=None,amount=None):
        trainer1=ctx.message.author
        if trainer2==None:
            await ctx.send("`Syntax: c!share <@mention> <amount>`")
            return
        if trainer2.bot==True:
            await ctx.send("Don't mention a bot.")
            return
        if amount==None:
            await ctx.send("`Syntax: c!share <@mention> <amount>`")
            return
        try:
            amount=int(amount)
        except:
            await ctx.send("`Syntax: c!share <@mention> <amount>`")
            return
        giver=db2_collection.find_one({"id": trainer1.id})
        taker=db2_collection.find_one({"id": trainer2.id})
        if giver==None:
            await ctx.send("`Oops, Seems like you don't have an account`")
            return
        if taker==None:
            await ctx.send(f"`Oops, Seems like **{trainer2.name}** doesn't have an account`")
            return
        if giver["Credits"]<amount:
            await ctx.send("`Looks like you don't have enough balance. Balance : {:,.0f} cc`".format(giver['Credits']))
            return
        giver["Credits"]-=amount
        taker["Credits"]+=amount
        db2_collection.update_one({"id":trainer2.id},{"$set":{"Credits": taker["Credits"]}})
        db2_collection.update_one({"id":trainer1.id},{"$set":{"Credits": giver["Credits"]}})
        await ctx.send("`Money transfer succesful, Current balance: {:,.0f} cc`".format(giver['Credits']))
def setup(bot):
	bot.add_cog(share(bot))
