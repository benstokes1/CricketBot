import discord 
import asyncio
import random 
from discord.ext import commands
class allow(commands.Cog):
  def __init__(self,bot):
      self.bot=bot
def setup(bot):
	  bot.add_cog(allow(bot))
