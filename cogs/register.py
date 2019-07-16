import discord 
import asyncio
import random 
from discord.ext import commands
class register(commands.Cog):
	def __init__(self,bot):
		global welcome_channel
		self.bot=bot
	@commands.command(aliases=["r"])
	async def register(self,ctx):
		await ctx.send("Seems like u have already registered :thinking:")
		with open("register.txt","r") as f1:
			for i in f1:
				if ctx.message.author.id==int(i):
					await ctx.send("Seems like u have already registered :thinking:")
					return
		with open("register.txt","a") as f:		
			f.write(str(ctx.message.author.id))
			await ctx.send(f"{ctx.message.author.mention} registered succesfully")
					
    
def setup(bot):
	bot.add_cog(register(bot))    
