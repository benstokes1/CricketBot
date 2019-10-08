import discord 
import asyncio
import random 
from discord.ext import commands
c=0
class duel(commands.Cog):
	def __init__(self,bot):
		global c
		self.bot=bot
	@commands.command(aliases=["sd"])

	async def start_duel(self,ctx,mem:discord.Member=None):
		
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
			if mem==None:
				await ctx.send("```Syntax: b!sd <@mention>(trainer name)```")
				return
			for i in ctx.message.guild.text_channels:
				global c
				k=i.name.lower().split("-")
				
				h=rolez.name.lower().split(" ")
				
				if k[0]==h[0]:
					c+=1
	@commands.command(aliases=["ed"])
	async def end_duel(self,ctx,mem:discord.Member=None):
		
		
		
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
			global c
			print(c)
			if mem==None:
				await ctx.send("```Syntax: b!ed <@mention>(trainer name)```")
				return
			if c==0:
				
				await ctx.send("*smh* You didnt start a battle!")
				return
			await ctx.send(f"GG! {mem.mention}")
			for i in ctx.message.guild.text_channels:
				k=i.name.lower().split("-")
				
				h=rolez.name.lower().split(" ")
				if k[0]==h[0]:
					if len(i.topic)==0:
						await i.edit(topic=f"1-{mem.name}")
					else:
						temp=i.topic.split("-")
						temp=int(i[0])+1
						print(temp)
						await i.edit(topic=f"{temp}-{mem.name}")
		c=0						
def setup(bot):
	bot.add_cog(duel(bot))
