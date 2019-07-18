import discord 
import asyncio
import random 
from discord.ext import commands


class register(commands.Cog):
	def __init__(self,bot):
		
		self.bot=bot
	@commands.command()
	async def register(self,ctx):
		for j in (ctx.author.roles):
			if j.name.lower()=="quiz":
				role = discord.utils.get(user.guild.roles,name="registered")
				await ctx.send(f"{ctx.message.author.mention} registered successfully")	
				await user.author.add_roles(role)
				return
		for j in (ctx.author.roles):
			if j.name.lower()=="registered":
				await ctx.send("Seems like u have registered already :thinking:")
				return		
		await ctx.send("Pay 100c to Void to register your name")
		
		
		
		
		
		
		
	
			
					
    
def setup(bot):
	bot.add_cog(register(bot))    
