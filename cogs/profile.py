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
class about(commands.Cog):
	def __init__(self,bot):
        	self.bot=bot
	@commands.command(aliases=["about"])
	@commands.guild_only()
	async def profile(self,ctx,user:discord.Member=None):
		if user==None:
			User=ctx.message.author
		else:
			User=user
		x=db2_collection.find_one({"id": User.id})
		if x==None:
			if user==None:
				await ctx.send("Create an account by typing `c!register`")
				return
			else:
				await ctx.send(f"Looks like {User.name} doesnt have an account")
		else:
			embed=discord.Embed()
			embed.set_thumbnail(url=f"{User.avatar_url}")
			embed.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator}",icon_url=f"{ctx.author.avatar_url}")
			embed.add_field(name="About",value=f"{x['about']}",inline=False)
			embed.add_field(name="Matches played",value=f"{x['matches_played']}",inline=False)
			embed.add_field(name="Matches won",value=f"{x['won']}",inline=False)
			embed.add_field(name="Matches lost",value=f"{x['lost']}",inline=False)
			if x["matches_played"]==0:
				win=0
			else:
				win=(x['won']/x["matches_played"])*100

			embed.add_field(name="Win percentage",value="{:.2f}%".format(win),inline=False)
			if len(x['recent_results'])==0:
				rs="-"
			else:
				rs=' '.join(x['recent_results'])
			embed.add_field(name="Recent results",value=rs)
			embed.set_footer(text=f"Current streak: {x['current_streak']}  Highest streak: {x['highest_streak']}")
			await ctx.send(embed=embed)
def setup(bot):
	bot.add_cog(about(bot))
