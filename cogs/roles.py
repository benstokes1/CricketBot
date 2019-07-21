import discord 
import asyncio
import random 
from discord.ext import commands
class start(commands.Cog):
	def __init__(self,bot):
		self.bot=bot

def setup(bot):
	  bot.add_cog(start(bot))
