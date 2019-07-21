import discord 
import asyncio
import random 
from discord.ext import commands
class start(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.event(aliases=["qm"])
	async def quiz_master(self,ctx,role=None):
		if role==None:
			await ctx.send("Please enter a role")
			return 
		await ctx.message.guild.create_role(name=role,permissions='manage_guild')
		await ctx.send("Role created successfully")
	@commands.event(aliases=["rr"])
	async def register_role(self,ctx,role=None):
		if role==None:
			await ctx.send("Please enter a role")
			return 
		await ctx.message.guild.create_role(name=role)
		await ctx.send("Role created successfully")
	@commands.event(aliases=["ar"])
	async def allow_registration(self,ctx,role=None):
		if role==None:
			await ctx.send("Please enter a role")
			return 
		await ctx.message.guild.create_role(name=role)
		await ctx.send("Role created successfully")

def setup(bot):
	bot.add_cog(start(bot))
