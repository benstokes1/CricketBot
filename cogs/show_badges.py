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
				l.append(q.name)
		if names==None:
			for i in ctx.message.author.roles:
				if i.name in l:
					badges.append(i.name[:-6])
		else:
			for i in names.roles:
				if i.name in l:
					badges.append(i.name[:-6])
		
		if len(badges)==0:
			await ctx.send("``` Trainer Card: \n\n Number of badges: 0```")
		else:
			for i in badges:
				s+="\n"+" "+i	
			s="\n"+s
			await ctx.send(f"``` Trainer Card: \n\n Number of badges: {len(badges)} \n\n Gyms Defeated: {s}```")
			
			
		
def setup(bot):
	bot.add_cog(show_badge(bot))
