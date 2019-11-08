import discord 
import asyncio
import random 
from discord.ext import commands
import json
class gym_leaders(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.command(aliases=["gl"])
	async def gym_leaders(self,ctx,names:discord.Member=None):
		with open("./cogs/json/data.txt","r") as hh:
			data=json.load(hh)
		l=data.keys()
		leader=""
		s=[] 
		for i in l:
			for t in self.bot.get_all_members():
				if str(t.id)==data[n]["leader_id"]:
						s.append(t.name)
		for i in len(l):
			leaders+=" "+"**"+data[l[i]]["gym_name"]+"**"+\n+" "+"Leader : "+s[i]+\n
		embed=discord.Embed(colour=10181046)
		embed.add_field(name="Leaders List",value="leaders")
def setup(bot):
	bot.add_cog(gym_leaders(bot))
