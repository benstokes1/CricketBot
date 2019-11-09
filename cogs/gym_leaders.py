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
		with open("./cogs/json/data.json","r") as hh:
			data=json.load(hh)
		l=data.keys()
		leader=""
		s=[] 
		for i in l:
			for t in self.bot.get_all_members():
				if str(t.id)==data[i]["leader_id"]:
					print(i)
					print(t.id)
					leader+=" "+"**"+data[i]['gym_name']+"**"+"\n"+" "+"Leader : "+"`"+t.name+"`"+"\n"+"\n"
		embed=discord.Embed(colour=1146986)
		embed.add_field(name="Leaders List",value=f"\n{leader}")
		await ctx.send(embed=embed)
def setup(bot):
	bot.add_cog(gym_leaders(bot))
