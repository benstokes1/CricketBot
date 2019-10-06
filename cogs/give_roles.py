import discord 
import asyncio
import random 
from discord.ext import commands
class badge(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.command(aliases=["gb"])
	async def give_badge(self,ctx,name:discord.Member=None):
		rolez = discord.utils.get(message.guild.roles,name="gym leader")
		if role in ctx.message.author.roles:
			if name==None:
				await ctx.send("```Syntax: q!give_badge <@mention>```")
				return
			role = discord.utils.get(user.guild.roles,name=ctx.message.author.name[:-6]+"badge")
			await name.add_roles(role)
			await ctx.send(f"Congratulations {name.mention}!!")
		else:
			await ctx.send(f"Looks like you don't have the gym leader role")
def setup(bot):
	bot.add_cog(badge(bot))
