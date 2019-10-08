import discord 
import asyncio
import random 
from discord.ext import commands
c=None
class duel(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.command(aliases=["sd"])

	async def start_duel(self,ctx,mem:discord.Member=None):
		if mem==None:
			await ctx.send("```Syntax: b!sd <@mention>(trainer name)```")
			return
		await ctx.send(f"Good luck {mem.mention} uwu")
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
				k=i.name.lower().split("-")
				
				h=rolez.name.lower().split(" ")
				
				if k[0]==h[0]:
					c=i.topic
	@commands.command(aliases=["ed"])
	async def end_duel(self,ctx,mem:discord.Member=None):
		print(c)
		if c==None:
			await ctx.send("*smh* You didnt start a battle!")
			return
		if mem==None:
			await ctx.send("```Syntax: b!ed <@mention>(trainer name)```")
			return
		await ctx.send(f"GG! {mem.mention}")
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
				k=i.name.lower().split("-")
				
				h=rolez.name.lower().split(" ")
				if k[0]==h[0]:
					if len(c)==0:
						i.edit(topic=f"1-{mem.name}")
					else:
						temp=i.topic.split("-")
						temp=int(i[0])
						i.edit(topic=f"{temp}-{mem.name}")
		c=None			
global c					
def setup(bot):
	bot.add_cog(duel(bot))
