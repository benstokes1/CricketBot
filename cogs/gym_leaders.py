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
					leader+=" "+role.name+": "+q.name+"\n"
		await ctx.send(f"``` {m} Gym Leaders: {leader}```") 
def setup(bot):
	bot.add_cog(gym_leaders(bot))
