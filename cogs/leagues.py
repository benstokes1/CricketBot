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
class show_leagues(commands.Cog):
	def __init__(self,bot):
        	self.bot=bot
	@commands.command(aliases=["leagues"])
	@commands.guild_only()
	async def show_leagues(self,ctx,number=None):
		arr = os.listdir('./Teams')
		available_leagues=arr
		print(arr)
		list_of_leagues=""
		for i in range(len(available_leagues)):
			list_of_leagues+=str(i)+". "+available_leagues[i]+"\n"
		embed=discord.Embed(text="Leagues",description=available_leagues)
def setup(bot):
	bot.add_cog(show_leagues(bot))
