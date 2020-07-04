import discord 
import asyncio
from discord.ext import commands
import json
class store(commands.Cog):
	def __init__(self,bot):
        	self.bot=bot
	@commands.command(aliases=["s"])
	async def store(self,ctx,*,m=None):
def setup(bot):
	bot.add_cog(store(bot))
