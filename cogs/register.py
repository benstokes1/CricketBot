import discord 
import asyncio
import random 
from discord.ext import commands
register=[0]
class register(commands.Cog):
	def __init__(self,bot):
		global register
		self.bot=bot
	@commands.command(aliases=["r"])
	async def register(self,ctx):
		await ctx.send("Seems like u have already registered :thinking:")
		for i in register:
			if ctx.message.author.id==i:
				await ctx.send("Seems like u have registered already :thinking:")
				return		
		register.append(ctx.message.author.id)
		await ctx.send(f"{ctx.message.author.mention} registered successfully")
					
    
def setup(bot):
	bot.add_cog(register(bot))    
