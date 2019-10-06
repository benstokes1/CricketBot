import discord 
import asyncio
import random 
from discord.ext import commands
class badge(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.command(aliases=["gb"])
	async def give_badge(self,ctx,name:discord.Member=None):
		rolez = discord.utils.get(ctx.message.guild.roles,names="gym leader")
		if rolez in ctx.message.author.roles:
			if names==None:
				await ctx.send("```Syntax: q!give_badge <@mention>```")
				return
			role = discord.utils.get(ctx.message.guild.roles,name=ctx.message.author.name[:-6]+"badge")
			if role in names.roles:
				await ctx.send("They have already won over this gym"+ctx.message.author.name[:-6])
			else:
				await names.add_roles(role)
				await ctx.send(f"Congratulations {names.mention}!!")
		else:
			await ctx.send(f"Looks like you don't have the gym leader role")
def setup(bot):
	bot.add_cog(badge(bot))
