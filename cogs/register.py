import discord 
import asyncio
import random 
from discord.ext import commands
registers=[0]
class register(commands.Cog):
	def __init__(self,bot):
		global register
		self.bot=bot
	@commands.command(aliases=["r"])
	async def register(self,ctx):
		
		for i in registers:
			if ctx.message.author.id==i:
				await ctx.send("Seems like u have registered already :thinking:")
				return		
		registers.append(ctx.message.author.id)
		await ctx.send(f"{ctx.message.author.mention} registered successfully")
		
		user = ctx.message.author
		role = discord.utils.get(user.server.roles, name="registered")
		await user.add_roles(ctx.message.author, role)
					
    
def setup(bot):
	bot.add_cog(register(bot))    
