import discord 
import asyncio
import random 
from discord.ext import commands
class clear(commands.Cog):
	def __init__(self,bot):
		global welcome_channel
		self.bot=bot
	@commands.command(aliases=["r"])
	async def register(self,ctx):
		with f as open("register.txt","a"):
			for i in f:
				if ctx.message.author.id==int(i):
					await ctx.send("Seems like u have already registered :thinking:")
				else:
					f.write(str(ctx.message.author.id))
					await ctx.send(f"{ctx.message.author.mention} registered succesfully")
					
    
def setup(bot):
	bot.add_cog(clear(bot))    
