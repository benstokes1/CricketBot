import discord 
import asyncio
import random 
from discord.ext import commands


class register(commands.Cog):
	def __init__(self,bot):
		
		self.bot=bot
	@commands.command()
	async def register(self,ctx):
		role = discord.utils.get(user.guild.roles,name="quiz")
		for i in ctx.message.discord.guild.roles:
			if ~(ctx.author.has_role(role)):
				await ctx.send("Pay 100c to Void to register your name")
				return
		role = discord.utils.get(user.guild.roles,name="registered")		
		for i in registers:
			if ctx.message.author.has_role(role):
				await ctx.send("Seems like u have registered already :thinking:")
				return		
		registers.append(ctx.message.author.id)
		await ctx.send(f"{ctx.message.author.mention} registered successfully")
		
		user = ctx.message
		
		await user.author.add_roles(role)
	
			
					
    
def setup(bot):
	bot.add_cog(register(bot))    
