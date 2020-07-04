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
class select_team(commands.Cog):
	def __init__(self,bot):
        	self.bot=bot
	@commands.command(aliases=["show_teams","st","ct"])
	@commands.guild_only()
	async def select_team(self,ctx,key=None,*,about=None):
		with open ("./Teams/IPL.json") as f:
			d=json.load(f)
		available_teams=[]
		for i in d:
			available_teams.append(i)
		team_list=""
		for i in range(len(available_teams)):
			team_list+=str(i+1)+". "+available_teams[i]+"\n"
		if number==None:
			embed=discord.Embed(title="Teams",description=team_list)
			embed.set_footer(text="To select a team use `c!select_team <number>`")
			await ctx.send(embed=embed)
		else:
			try:
				number=int(number)-1
			except:
				return
			x=db_collection.find_one({"Team1_member_id": ctx.message.author.id})
			if x==None:
				x=db_collection.find_one({"Team2_member_id": ctx.message.author.id})
				if x==None:
					return
				else:
					player_list=""
					for i in range(len(d[available_teams[number]])):
						player_list+=str(i+1)+". "+d[available_teams[number]][i]+"\n"
					if x["Team2_name"]!="None":
						await ctx.send("Can't change your team once after u chose it")
						return
					if x["Team1_name"]!="None" and x["Team1_name"]==available_teams[number]:
						await ctx.send(f"The other player already chose {available_teams[number]}\nChoose an other team")
						return
					x["Team2_name"]=available_teams[number]
					db_collection.update_one({"Team2_member_id": ctx.message.author.id},{"$set":{"Team2_name":available_teams[number],"Team2_data.Lineup":d[available_teams[number]]}})
					embed=discord.Embed(title="Teams",description=player_list)
					await ctx.send(content=f"**{available_teams[number]}** selected\n`Heres the list of playin XI`",embed=embed)
					if x["Team2_name"]!="None" and x["Team1_name"]!="None":
						await ctx.send("Set the overs by typing `c!set_overs`")
						return
			else:
				if x["Team1_name"]!="None":
					await ctx.send("Can't change your team once after u chose it")
					return
				if x["Team2_name"]!="None" and x["Team2_name"]==available_teams[number]:
						await ctx.send(f"The other player already chose {available_teams[number]}\nChoose an other team")
						return
				x["Team1_name"]=available_teams[number]
				player_list=""
				for i in range(len(d[available_teams[number]])):
					player_list+=str(i+1)+". "+d[available_teams[number]][i]+"\n"
				db_collection.update_one({"Team1_member_id": ctx.message.author.id},{"$set":{"Team1_name":available_teams[number],"Team1_data.Lineup":d[available_teams[number]]}})
				embed=discord.Embed(title="Teams",description=player_list)
				await ctx.send(content=f"**{available_teams[number]}** selected\n`Here's the list of playing XI`",embed=embed)
				if x["Team2_name"]!="None" and x["Team1_name"]!="None":
					await ctx.send("Set the overs by typing `c!set_overs`")
					return

def setup(bot):
	bot.add_cog(select_team(bot))