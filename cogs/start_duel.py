import discord 
import asyncio
import random 
from discord.ext import commands
c=None
class duel(commands.Cog):
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
		else:
			for i in ctx.message.guild.text_channels:
				k=i.name.split("-")
				print(k)
				h=rolez.name.lower().split(" ")
				print(h)
				if k[0]==h[0]:
					c=i.topic
					
					
					
def setup(bot):
	bot.add_cog(duel(bot))
