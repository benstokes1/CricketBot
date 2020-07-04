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
class toss(commands.Cog):
	def __init__(self,bot):
        	self.bot=bot
	@commands.command(aliases=["t"])
	@commands.guild_only()
	async def toss(self,ctx,choice=None):
		
		#toss
		if choice==None:
			pass
		elif choice.title() not in ["Heads","Tails"]:
			await ctx.send("Syntax: `c!toss <opponent's call>`")
			return

		outcomes=["Heads","Tails"]
		answer=random.choice(outcomes)
		embed=discord.Embed(title='Toss')
		embed.set_image(url="https://i.pinimg.com/originals/d7/49/06/d74906d39a1964e7d07555e7601b06ad.gif")
		message=await ctx.send(embed=embed)
		await asyncio.sleep(5)	
		embed=discord.Embed(title=f'Oh! Its a {answer}')
		await message.edit(embed=embed)
		x=db_collection.find_one({"Team1_member_id": ctx.message.author.id})
		if x==None:
			x=db_collection.find_one({"Team2_member_id": ctx.message.author.id})
			if x==None:
				return
			else:
				if x["Maximum_overs"]==0:
					await ctx.send("Toss can be done only after setting overs")
					return
				if x["Score_card"]["Toss"]!=0:
					return
				if choice==None:
					return
				if x["Team1_member_id"]==ctx.message.author.id:
					caller=x["Team2_name"]
					tosser=x["Team1_name"]
				else:
					tosser=x["Team2_name"]
					caller=x["Team1_name"]
				if choice.title()==answer:
					x=db_collection.update_one({"Team2_member_id": ctx.message.author.id},{"$set":{"Score_card.Toss": x["Team1_member_id"]}})	
					await ctx.send(f"**{caller}** won the toss\n**Note:** Use `c!choose <bat/bowl>` to choose batting or bowling")
				else:
					x=db_collection.update_one({"Team2_member_id": ctx.message.author.id},{"$set":{"Score_card.Toss": x["Team2_member_id"]}})	
					await ctx.send(f"**{tosser}** won the toss\n**Note:** Use `c!choose <bat/bowl>` to choose batting or bowling")
		else:

			if x["Maximum_overs"]==0:
				await ctx.send("Toss can be done only after setting overs")
				return
			if x["Score_card"]["Toss"]!=0:
				return
			if choice==None:
				return
			if x["Team1_member_id"]==ctx.message.author.id:
				caller=x["Team2_name"]
				tosser=x["Team1_name"]
			else:
				tosser=x["Team2_name"]
				caller=x["Team1_name"]
			if choice.title()==answer:
				x=db_collection.update_one({"Team1_member_id": ctx.message.author.id},{"$set":{"Score_card.Toss": x["Team2_member_id"]}})	
				await ctx.send(f"**{caller}** won the toss\n**Note:** Use `c!choose <bat/bowl>` to choose batting or bowling")
			else:
				x=db_collection.update_one({"Team1_member_id": ctx.message.author.id},{"$set":{"Score_card.Toss": x["Team1_member_id"]}})	
				await ctx.send(f"**{tosser}** won the toss\n**Note:** Use `c!choose <bat/bowl>` to choose batting or bowling")
def setup(bot):
	bot.add_cog(toss(bot))
