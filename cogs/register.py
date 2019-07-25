import discord 
import asyncio
import random 
from discord.ext import commands


class register(commands.Cog):
	def __init__(self,bot):
		
		self.bot=bot
	@commands.command()
	async def register(self,ctx):
		user=ctx.message
		role = discord.utils.get(user.guild.roles,name="registered")
		
		if role in ctx.author.roles:
			await ctx.send("Seems like u have registered already :thinking:")
			return
		
		
		await ctx.send(f"{ctx.message.author.mention} registered successfully")	
		await user.author.add_roles(role)
		
				
		
		
		
		
		
		
		
		
	
			
					
    
def setup(bot):
	bot.add_cog(register(bot))    
