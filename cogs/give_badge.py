import discord 
import asyncio
import random 
from discord.ext import commands
import json
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
	
		for k in ctx.message.guild.roles:
			if k.name.lower().endswith("gym badge"):
				f=k.name.lower().split(" ")
				if f[0]==i[0]:
					role=k
					break
		if role in names.roles:
		
			await ctx.send("They have already won over "+role.name[:-6])
		else:
		
			await names.add_roles(role)
			with open("./cogs/json/data.txt","r") as hh:
				data=json.load(hh)
			data[i[0]['h_o_f']].append(names.name)
			data[i[0]['n_o_w']]=str(int(data[i[0]['n_o_w']])-1)
			data[i[0]['b']]=str(int(data[i[0]['b']])-100)
			with open("./cogs/json/data.txt","w") as hh:
				json.dump(data,hh)
			await ctx.send(f"Congratulations {names.mention}!!"+"\n"+f"Your name has been added to the hall of fame of {role.name.upper()[:-6]}\nType `b!tc` to see the list of badges")
def setup(bot):
	bot.add_cog(badge(bot))
