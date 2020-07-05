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
				original_name=Team2.name
				h=db2_collection.find_one({"id":Team2_id})
			await ctx.send(f"**{original_name}** finish your undone match with **{h['now_match']}** or type `c!end` to end the match")
			return
		x=db_collection.find_one({"Team1_member_id": Team1_id})
		if x==None:
			x=db_collection.find_one({"Team2_member_id": Team1_id})
			if x==None:
				return
			else:
				if x["status"]==0:
					db_collection.update_one({"Team2_member_id": Team1_id},{"status": 1})
				      	await ctx.send("Select Teams by typing `c!select_team`")
				       	return
				else:
				       	return
		else:
			if x["status"]==0:
				db_collection.update_one({"Team2_member_id": Team1_id},{"status": 1})
				await ctx.send("Select Teams by typing `c!select_team`")
				return
			else:
				return
		
		opponent_1=ctx.message.author.name+"#"+str(ctx.message.author.discriminator)
		db2_collection.update_one({"id": Team2_id},{"$set":{"now_match": opponent_1}})
		opponent_1=Team2.name+"#"+Team2.discriminator
		db2_collection.update_one({"id":Team1_id},{"$set":{"now_match": opponent_1}})
		outline={
		"league" : "None",
	    "Team1_name": "None",
	    "Team2_name": "None",
	    "Team1_member_id": Team1_id,
	    "Team2_member_id": Team2_id,
		"Maximum_overs":0,
		"Now_batting": 0,
	    "Team1_data":{
		"Lineup":[],
		"Batting": {},
		"Bowling": {},
			"Current_batting": [],
			"Current_bowling": [],
			"Previous_bowler": [],
		"Batsmen_out": []
	    },
	    "Team2_data":{
		"Lineup":[],
		"Batting": {},
		"Bowling": {},
			"Current_batting": [],
			"Current_bowling": [],
			"Previous_bowler": [],
		"Batsmen_out": []
	    },
		"Score_card": {
				"Target": 0,
				"Overs": "0.0",
				"Maximum_overs": "0.0",
				"Last_ball": "0",
				"Score": 0,
				"Wickets": 0,
				"Toss": 0,
				"First_innings_score": "0" 
			} ,
	    "First_innings_score": "",
	    "This_over": "",
		"Maximum_wickets": 10
		}
		db1_collection.update_one({},{"$set":{"ids":x['ids']}})
		db_collection.insert_one(outline)
		await ctx.send("Select Teams by typing `c!select_team`")
def setup(bot):
	bot.add_cog(accept(bot))'''
