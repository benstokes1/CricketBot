import discord 
import asyncio
import random 
from discord.ext import commands
class clear(commands.Cog):
	def __init__(self,bot):
		global welcome_channel
		self.bot=bot
    
def setup(bot):
	bot.add_cog(clear(bot))    
