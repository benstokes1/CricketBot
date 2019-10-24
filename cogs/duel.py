import discord 
import asyncio
from discord.ext import commands
c=0
class duel(commands.Cog):
	def __init__(self,bot):
		global c
		self.bot=bot
	@commands.command(aliases=["sd"])

	async def start_duel(self,ctx,mem:discord.Member=None):
		
		
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
			await ctx.send(f"Good luck {mem.mention} uwu")
			h=rolez.name.lower().split(" ")
			for i in ctx.message.guild.text_channels:
				global c
				k=i.name.lower().split("-")
				
				
				
				if h[0] in k[0]:
					c+=1
					if i.topic==None:
						break
					elif len(i.topic)==0:
						break
					else:	
						temp=i.topic.split("-")
						if int(temp[1])!=ctx.message.author.id:
							await i.edit(topic=f"0-{ctx.message.author.id}-{mem.id}")
					break
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
			if mem==None:
				await ctx.send("```Syntax: b!ed <@mention>(trainer name)```")
				return
			if c==0:
				await ctx.send("*smh* You didnt start a battle!")
				return
			await ctx.send(f"GG! {mem.mention}")
			h=rolez.name.lower().split(" ")
			for i in ctx.message.guild.text_channels:
				k=i.name.lower().split("-")
				if h[0] in k[0]:
					
					if i.topic==None:
						await i.edit(topic=f"1-{ctx.message.author.id}-{mem.id}")
					elif len(i.topic)==0:
						await i.edit(topic=f"1-{ctx.message.author.id}-{mem.id}")
					else:
						temp=i.topic.split("-")
						
						temp=int(temp[0])+1
						
						await i.edit(topic=f"{temp}-{ctx.message.author.id}-{mem.id}")
					break
		c=0						
def setup(bot):
	bot.add_cog(duel(bot))
