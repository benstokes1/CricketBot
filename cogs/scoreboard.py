import discord 
import asyncio
import random
from discord.ext import commands
import os
import datetime
import pymongo
import json
import math
m=None
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
		global m
		x=db_collection.find_one({"Team1_member_id": ctx.message.author.id})
		if x==None:
			x=db_collection.find_one({"Team2_member_id": ctx.message.author.id})
			if x==None:
				return
			else:
				if x["Now_batting"]==x["Team1_member_id"]:
					Batting_team=x["Team1_data"]
					Batting_team_name=x["Team1_name"]
					Bowling_team=x["Team2_data"]
					Bowling_team_name=x["Team2_name"]
				else:
					Batting_team=x["Team2_data"]
					Bowling_team=x["Team1_data"]
					Batting_team_name=x["Team2_name"]
					Bowling_team_name=x["Team1_name"]
		else:
			if x["Now_batting"]==x["Team1_member_id"]:
				Batting_team=x["Team1_data"]
				Batting_team_name=x["Team1_name"]
				Bowling_team=x["Team2_data"]
				Bowling_team_name=x["Team2_name"]
			else:
				Batting_team=x["Team2_data"]
				Bowling_team=x["Team1_data"]
				Batting_team_name=x["Team2_name"]
				Bowling_team_name=x["Team1_name"]
		
		Batting_players=Batting_team["Lineup"]
		Bowling_players=Bowling_team["Bowling"]
		out_batting="```"+Batting_team_name+" Batting```\n"+"```{:<45}".format("Player")+"{}```".format("Runs")
		out_bowling="```"+Bowling_team_name+" Bowling```\n"+"```{:<25}".format("Player")+"{:<15}{:<15}".format("Overs","Economy")+"{}```".format("Figures")
		for i in Batting_players:
			if i in Batting_team["Batting"]:
				if i in Batting_team["Current_batting"]:
					out_batting+="```{:<25}".format(i)+"{:<20}".format("notout")+"{}({})```".format(Batting_team["Batting"][i]["runs"],Batting_team["Batting"][i]["balls_faced"])
				if i in Batting_team['Batsmen_out']:
					out_batting+="```{:<25}".format(i)+"{:<20}".format("out")+"{}({})```".format(Batting_team["Batting"][i]["runs"],Batting_team["Batting"][i]["balls_faced"])
			else:
				out_batting+="```{:<25}```".format(i)
		score_board=x["Score_card"]
		if score_board["Target"]!=0:
			balls_reamining=score_board["Overs"].split(".")
			balls_reamining=int(balls_reamining[0])*6+int(balls_reamining[1])
			balls_reamining=x["Maximum_overs"]*6-balls_reamining
			out_batting+="```"+Batting_team_name+" needs "+str(score_board["Target"]-score_board["Score"])+" from "+str(balls_reamining)+".```"
		for i in Bowling_players:
			balls_thrown=str(Bowling_players[i]["balls_thrown"]//6)+"."+str(Bowling_players[i]["balls_thrown"]%6)
			try:
				economy=Bowling_players[i]["runs"]/float(balls_thrown)
			except:
				economy=0.00
			economy="%.2f"%(economy)
			out_bowling+="```{:<25}".format(i)+"{:<15}{:<15}".format(balls_thrown,economy)+"{}/{}```".format(Bowling_players[i]["runs"],Bowling_players[i]["wickets"])
		output=[out_batting,out_bowling]
		count=0
		m=await ctx.send(output[0])
		await m.add_reaction("⬅️")
		await m.add_reaction("➡️")
		def check(reaction, user):
			return (user.id==ctx.message.author.id and m.id==reaction.message.id)
		while 1:
			try:
				reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
			except asyncio.TimeoutError:
				return        
			else:
				m = await ctx.channel.fetch_message(m.id)
				if str(reaction.emoji)=="➡️":
					count+=1
					if count>len(output)-1:
						count=0
					await m.edit(content=output[count])
					await m.remove_reaction("➡️",user)
				elif str(reaction.emoji)=="⬅️":
					count-=1
					if count==-1:
						count=len(output)-1
					await m.edit(content=output[count])
					await m.remove_reaction("⬅️",user)
				else:
					await m.remove_reaction(str(reaction.emoji),user)
				

def setup(bot):
	bot.add_cog(score_board(bot))
