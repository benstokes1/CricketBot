import discord 
import asyncio
from discord.ext import commands
c=0
class duel(commands.Cog):
	def __init__(self,bot):
		global c
		self.bot=bot
	@commands.command(aliases=["r"])

	async def random(self,ctx,mem:discord.Member=None):					
def setup(bot):
	bot.add_cog(random(bot))
