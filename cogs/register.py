import discord 
import asyncio
import random 
from discord.ext import commands
registers=[0]
class register(commands.Cog):
	def __init__(self,bot):
		global register
		self.bot=bot
	@commands.command()
	async def register(self,ctx):
		
		for i in registers:
			if ctx.message.author.id==i:
				await ctx.send("Seems like u have registered already :thinking:")
				return		
		registers.append(ctx.message.author.id)
		await ctx.send(f"{ctx.message.author.mention} registered successfully")
		
		user = ctx.message
		role = discord.utils.get(user.guild.roles,name="registered")
		await user.author.add_roles(role)
	@commands.command()
	async def allow(self,ctx,member:discord.Member):
		role = discord.utils.get(user.guild.roles,name="quiz")
		await member.add_roles(role)
			
					
    
def setup(bot):
	bot.add_cog(register(bot))    
