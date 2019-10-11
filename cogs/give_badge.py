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
		rolez=None
		for q in ctx.message.guild.roles:
			if q.name.lower().endswith("gym leader"):
				l.append(q)
		for i in l:
			if i in ctx.message.author.roles:
				rolez=i
				break
		
		if names==None:
			await ctx.send("```Syntax: b!give_badge <@mention>```")
			return
		if rolez==None:
			await ctx.send(f"Looks like you are not a gym leader")
			return
		i=rolez.name.lower().split(" ")
		for k in names.roles:
			if k.name.lower().endswith("gym badge"):
				f=k.name.lower().split(" ")
				if f[0]==i[0]:
					role=k
					break
		if role in names.roles:
			print("a")
			await ctx.send("They have already won over "+role.name[:-6])
		else:
			print("b")
			await names.add_roles(role)
			await ctx.send(f"Congratulations {names.mention}!!"+"\n"+f"Your name has been added to the hall of fame of {role.name.upper()[:-6]}\nType `b!tc` to see the list of badges")
def setup(bot):
	bot.add_cog(badge(bot))
