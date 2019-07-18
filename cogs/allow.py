import discord 
import asyncio
import random 
from discord.ext import commands
class allow(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.command()
	async def allow(self,ctx,member:discord.Member):
	
		role = discord.utils.get(member.guild.roles,name="quiz")
		await member.add_roles(role)
		await ctx.send(f"{member.mention}Please register to participate in the quiz")
def setup(bot):
	bot.add_cog(allow(bot))
