import discord 
import asyncio
import random 
from discord.ext import commands
class show_badge(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.command(aliases=["sb"])
	async def show_badge(self,ctx,names:discord.Member=None):
		l=[]
		badges=[]
		s=""
		for q in ctx.message.guild.roles:
			if q.name.lower().endswith("gym badge"):
				l.append(q.name[:-7])
		if names==None:
			for i in ctx.message.author.roles:
				if i in l:
					badges.append(i.name)
		else:
			for i in names.roles:
				if i in l:
					badges.append(i.name)
		if len(badges)==0:
			await ctx.send("``` Badge Pouch: \n Number of badges: 0```")
		else:
			for i in badges:
				s+="\n"+" "+badges[i[:-6]]	
			await ctx.send(f"``` Badge Pouch: \n Number of badges: {len(badges)} \n Gyms Defeated: {s}```")
			
			
		
def setup(bot):
	bot.add_cog(show_badge(bot))
