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
		if rolez==None:
			await ctx.send(f"Looks like you are not a gym leader")
			return
		
		h=rolez.name.lower().split(" ")
		with open("./cogs/json/data.json","r") as hh:
				data=json.load(hh)
		with open("./cogs/json/data1.json","r") as hr:
				data1=json.load(hr)
		for i in list(data.keys()):
			if data[i]['leader_id']==str(ctx.message.author.id):
				print("avl")
				await ctx.send("But u already own an account")
				return
		print("sa")
		if h[0] in data.keys():					
			print("sa")
			hof=data[h[0]]['h_o_f']
			hofi=data[h[0]]['h_o_f_i']
			data[h[0]]=data1['i']
			data[h[0]]['h_o_f']=hof
			data[h[0]]['h_o_f_i']=hofi
		else:
			data[h[0]]=data1['i']
			print("sa")

		data[h[0]]['leader_id']=str(ctx.message.author.id)
		
		data[h[0]]['gym_name']=p+" Type Gym"
		
		print("Sa")
		with open("./cogs/json/data.json","w") as hh:
			json.dump(data,hh)
		print(data)

		await ctx.send("Account created successfully..Good luck!")
			
					
					
		
def setup(bot):
	bot.add_cog(create_account(bot))
