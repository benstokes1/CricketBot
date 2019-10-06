import discord 
import asyncio
import random 
from discord.ext import commands
class gym_leaders(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.command(aliases=["gl"])
	async def gym_leaders(self,ctx,names:discord.Member=None):
		leader= ""
		for q in self.bot.get_all_members():
			for role in q.roles:
				if role.name.endswith(" gym leader"):
					leader+="\n"+" "+role.name.upper()+": "+q.name+"\n"
		leeader="\n\n"+leader
		x=Gym Leaders: +"\n"
		await ctx.send(f"```{x} {leader}```") 
def setup(bot):
	bot.add_cog(gym_leaders(bot))