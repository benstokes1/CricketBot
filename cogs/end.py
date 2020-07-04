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
class end(commands.Cog):
	def __init__(self,bot):
        	self.bot=bot
	@commands.command()
	@commands.guild_only()
	async def end(self,ctx):
		x=db_collection.find_one({"Team1_member_id": ctx.message.author.id})
		try:
			if x==None:
				x=db_collection.find_one({"Team2_member_id": ctx.message.author.id})
				if x==None:
					await ctx.send("No matches are running")
					return
				else:
					xy=db1_collection.find_one()
					team1_member=None
					for i in self.bot.guilds:
						for j in i.members:
							if x["Team1_member_id"]==j.id:
								team1_member=j
								break
						if team1_member!=None:
							break
					team2_member=ctx.message.author
					db2_collection.update_one({"id": team2_member.id},{"$set":{"now_match" :""}})
					db2_collection.update_one({"id": x["Team1_member_id"]},{"$set":{"now_match" :""}})
					if team1_member==None:
						team1_member.id=x["Team1_member_id"]
						db_collection.delete_one({"Team2_member_id":team2_member.id})
						xy["ids"].pop(xy["ids"].index(team1_member.id))
						xy["ids"].pop(xy["ids"].index(team2_member.id))
						db1_collection.update_one({},{"$set":{"ids":x["ids"]}})
						await ctx.send("Match abandoned successfully")
						return				
					db_collection.delete_one({"Team2_member_id":team2_member.id})
					xy["ids"].pop(xy["ids"].index(team1_member.id))
					xy["ids"].pop(xy["ids"].index(team2_member.id))
					db1_collection.update_one({},{"$set":{"ids":xy["ids"]}})
					await ctx.send("Match abandoned successfully")
					if team2_member.dm_channel==None:
						await team2_member.create_dm()	
					if team1_member.dm_channel==None:
						await team1_member.create_dm()
					dm1=team2_member.dm_channel
					dm2=team1_member.dm_channel			
					await dm1.send(f"Match between **{team1_member.name}#{team1_member.discriminator}** vs **{team2_member.name}#{team2_member.discriminator}** has been abandoned by {ctx.message.author.name}#{ctx.message.author.discriminator}")
					await dm2.send(f"Match between **{team1_member.name}#{team1_member.discriminator}** vs **{team2_member.name}#{team2_member.discriminator}** has been abandoned by {ctx.message.author.name}#{ctx.message.author.discriminator}")
			else:
				xy=db1_collection.find_one()
				team2_member=None
				for i in self.bot.guilds:
					for j in i.members:
						if x["Team2_member_id"]==j.id:
							team2_member=j
							break
					if team2_member!=None:
						break
				team1_member=ctx.message.author
				db2_collection.update_one({"id": team1_member.id},{"$set":{"now_match" :""}})
				db2_collection.update_one({"id": x["Team2_member_id"]},{"$set":{"now_match" :""}})
				if team2_member==None:
					team2_member.id=x["Team2_member_id"]

					db_collection.delete_one({"Team1_member_id":team1_member.id})
					xy["ids"].pop(xy["ids"].index(team1_member.id))
					xy["ids"].pop(xy["ids"].index(team2_member.id))
					db1_collection.update_one({},{"$set":{"ids":x["ids"]}})
					await ctx.send("Match abandoned successfully")
					return

				db_collection.delete_one({"Team1_member_id":team1_member.id})
				xy["ids"].pop(xy["ids"].index(team1_member.id))
				xy["ids"].pop(xy["ids"].index(team2_member.id))
				db1_collection.update_one({},{"$set":{"ids":xy["ids"]}})
				await ctx.send("Match abandoned successfully")

				if team2_member.dm_channel==None:
					await team2_member.create_dm()
				if team1_member.dm_channel==None:
					await team1_member.create_dm()
				dm1=team2_member.dm_channel
				dm2=team1_member.dm_channel
				await dm1.send(f"Match between **{team1_member.name}#{team1_member.discriminator}** vs **{team2_member.name}#{team2_member.discriminator}** has been abandoned by {ctx.message.author.name}#{ctx.message.author.discriminator}")
				await dm2.send(f"Match between **{team1_member.name}#{team1_member.discriminator}** vs **{team2_member.name}#{team2_member.discriminator}** has been abandoned by {ctx.message.author.name}#{ctx.message.author.discriminator}")

		except:
			pass

def setup(bot):
	bot.add_cog(end(bot))
