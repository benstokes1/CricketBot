import discord 
import asyncio
import random 
from discord.ext import commands
import json
class create_account(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.command(aliases=["ca"])
	async def create_account(self,ctx):
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
		
		h=rolez.name.lower().split(" ")
	
		with open("./cogs/json/data.json","r") as hh:
				data=json.load(hh)
		with open("./cogs/json/data1.json","r") as hh:
				data1=json.load(hh)
		for i in data.keys():
			if data[i]['leader_id']==str(ctx.message.author.id):
				await ctx.send("But u already own an account")
				return
			data[h[0]]=data1
			data[h[0]]['leader_id']=str(ctx.message.author.id)
			data[h[0]]['gym_name']=h[0].sentence()+" Type Gym"
			with open("./cogs/json/data.json","w") as hh:
				json.dump(data,hh)
			await ctx.send("Account created successfully..Good luck!")
			
					
					
		
def setup(bot):
	bot.add_cog(create_account(bot))
