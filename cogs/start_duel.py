import discord 
import asyncio
import random 
from discord.ext import commands
class start_duel(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.command(aliases=["sd"])
	async def start_duel(self,ctx):
		l=[]
		rolez=None
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
		
		if role in names.roles:
			await ctx.send("They have already won over "+role.name[:-6])
		else:
			await names.add_roles(role)
			await ctx.send(f"Congratulations {names.mention}!!"+"\n"+f"Your name has been added to the hall of fame of {role.name.upper()[:-6]}\nType `b!sb` to see the list of badges")
def setup(bot):
	bot.add_cog(start_duel(bot))
