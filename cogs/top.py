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
class top(commands.Cog):
	def __init__(self,bot):
        	self.bot=bot
	@commands.command()
	@commands.guild_only()
	async def top(self,ctx,m=None):
		x=db2_collection.find().sort([("won",-1),("winning_percentage",-1)])
		top_players=[]
		if m.lower()=="server":
			for j in x:
				if len(top_players)==5:
					break
				for i in ctx.message.guild.members:
					if i.id==j["id"]:
						string=i.name+"#"+str(i.discriminator)+"\n"+"Wins: "+str(j["wins"])+"\n"
						top_players.append(string)
						break
			p=""
			for i in range(len(top_players)):
				p+=str(i+1)+". "+top_players[i]+"\n"	
			embed=discord.Embed(title="Top players",description=p)
			await ctx.send(embed=embed)
		elif m.lower()=="global":
			for j in x:
				if len(top_players)==5:
					break
				
				l=None
				for i in self.bot.guilds:
					l=i.get_member(j["id"])
					if l!=None:
						break
				if l==None:
					pass
				else:
					string=l.name+"#"+str(l.discriminator)+"\n"+"Wins: "+str(j["wins"])+"\n"
					top_players.append(string)
			p=""
			for i in range(len(top_players)):
				p+=str(i+1)+". "+top_players[i]+"\n"	
			embed=discord.Embed(title="Top players",description=p)
			await ctx.send(embed=embed)
def setup(bot):
	bot.add_cog(top(bot))
