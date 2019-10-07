import discord 
import asyncio
import random 
from discord.ext import commands
class badge(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.command(aliases=["gb"])
	async def give_badge(self,ctx,names:discord.Member=None):
		l=[]
		for q in ctx.message.guild.roles:
			if q.name.lower().endswith("gym leader"):
				l.append(q)
		for i in l:
			if i in ctx.message.author.roles:
				rolez=i
				break
		if rolez==None:
			await ctx.send(f"Looks like you are not a gym leader")
			return
		if names==None:
			await ctx.send("```Syntax: b!give_badge <@mention>```")
			return
		role = discord.utils.get(ctx.message.guild.roles,name=rolez.name[:-6]+"badge")
		if role in names.roles:
			await ctx.send("They have already won over "+role.name[:-6])
		else:
			await names.add_roles(role)
			await ctx.send(f"Congratulations {names.mention}!!"+"\n"+f"Your name has been added to the hall of fame of {role.name.upper()[:-6]}")
def setup(bot):
	bot.add_cog(badge(bot))
