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
class score_board(commands.Cog):
	def __init__(self,bot):
        	self.bot=bot
	@commands.command(aliases=["scorecard","sb"])
	@commands.guild_only()
	async def scoreboard(self,ctx):
		x=db_collection.find_one({"Team1_member_id": ctx.message.author.id})
		if x==None:
			x=db_collection.find_one({"Team2_member_id": ctx.message.author.id})
			if x==None:
				return
			else:
				x=x["Score_card"]
				if x["Target"]==0:
					embed=discord.Embed(title="Scoreboard",description=f"**First Innings Score :**\nScore : {x['Score']}/{x['Wickets']}\nOvers : {x['Overs']}/{x['Maximum_overs']}")
					await ctx.send(embed=embed)
					return
				else:
					embed=discord.Embed(title="Scoreboard",description=f"**Target :** {x['Target']}\n**Overs :** {x['Overs']}/{x['Maximum_overs']}\n\n**First Innings Score :**\nScore : {x['First_innings_score']}\n\n**Second Innings Score :**\nScore : {x['Score']}/{x['Wickets']}")
					await ctx.send(embed=embed)
					return
		else:
			x=x["Score_card"]
			if x["Target"]==0:
				embed=discord.Embed(title="Scoreboard",description=f"**First Innings Score :**\nScore : {x['Score']}/{x['Wickets']}\nOvers : {x['Overs']}/{x['Maximum_overs']}")
				await ctx.send(embed=embed)
				return
			else:
				embed=discord.Embed(title="Scoreboard",description=f"**Target :** {x['Target']}\n**Overs :** {x['Overs']}/{x['Maximum_overs']}\n\n**First Innings Score :**\nScore : {x['First_innings_score']}\n\n**Second Innings Score :**\nScore : {x['Score']}/{x['Wickets']}")
				await ctx.send(embed=embed)
				return

def setup(bot):
	bot.add_cog(score_board(bot))
