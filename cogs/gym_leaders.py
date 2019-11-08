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
			leaders+=" "+"**"+data[l[i]]["gym_name"]+"**"+"\n"+" "+"Leader : "+s[i]+"\n"+"\n"
		embed=discord.Embed(colour=1146986)
		embed.add_field(name="Leaders List",value=f"\n{leaders}")
		await ctx.send(embed=embed)
def setup(bot):
	bot.add_cog(gym_leaders(bot))
