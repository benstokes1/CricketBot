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
class accept(commands.Cog):
	def __init__(self,bot):
        	self.bot=bot
	@commands.command()
	@commands.guild_only()
	async def accept(self,ctx):
		'''Team2_id=ctx.message.author.id
		h1=db2_collection.find_one({"id":ctx.message.author.id})
		if h1==None:
			if h1==None:
				await ctx.send("You need to have an account to challenge a person\nType `c!register` to create an account")
				return
		x=db1_collection.find_one()
		if x==None:
			pass
		elif ctx.message.author.id in x["ids"]:
			h=db2_collection.find_one({"id":ctx.message.author.id})
			original_name=ctx.author.name
			if h==None:
				pass
			else:	
				await ctx.send(f"**{original_name}** finish your undone match with **{h['now_match']}** or type `c!end` to end the match")
				return
		x=db_collection.find_one({"Team1_member_id": Team2_id})
		if x==None:
			x=db_collection.find_one({"Team2_member_id": Team2_id})
			if x==None:
				return
			else:
				if x["status"]==0:
				       	player1_name=ctx.message.guild.get_member(x["Team2_id"])
				       	player2_name=ctx.message.guild.get_member(x["Team1_id"])
				       	if player1_name==None or player2_name==None:
				       		await ctx.send("Select Teams by typing `c!select_team`")	
				       	else:
				       		await ctx.send(f"Duel between {player1_name} and {player2_name} has started\nSelect Teams by typing `c!select_team`")
					db_collection.update_one({"Team2_member_id": Team2_id},{"status": 1})
				else:
				       	return
		else:
			if x["status"]==0:
				player1_name=ctx.message.guild.get_member(x["Team2_id"])
				player2_name=ctx.message.guild.get_member(x["Team1_id"])
				if player1_name==None or player2_name==None:
					await ctx.send("Select Teams by typing `c!select_team`")	
				else:
					await ctx.send(f"Duel between {player1_name} and {player2_name} has started\nSelect Teams by typing `c!select_team`")
				db_collection.update_one({"Team2_member_id": Team2_id},{"status": 1})
			else:
				return
		o=db1_collection.find_one()
		o["ids"].append(x["Team1_member_id"])
		o["ids"].append(x["Team2_member_id"])
		db1_collection.update_one({},{"ids":o["ids"]})'''
def setup(bot):
	bot.add_cog(accept(bot))
