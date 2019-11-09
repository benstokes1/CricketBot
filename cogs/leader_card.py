import discord 
import asyncio
from discord.ext import commands
import json
import random
class leader_card(commands.Cog):
	def __init__(self,bot):
		
		self.bot=bot
	@commands.command(aliases=["lc"])

	async def leader_card(self,ctx,mem=None):
		
		
		l=[]
		p=None
		
		for q in ctx.message.guild.roles:
			if q.name.lower().endswith("gym leader"):
				m=q.name.lower().split(" ")
				l.append(m[0])
		
		with open("./cogs/json/data.json","r") as hh:
			data=json.load(hh)
		
			
		
	
		if mem==None:
		
			mem=ctx.message.author
		elif (mem not in l):
			await ctx.send("```Syntax: b!leader_card <name of gym(ex: fire)>(optional if u are a gym leader)```")
			return
		
		else:
			if mem not in data.keys():
				await ctx.send("No data found")
			else:
				
				mem=mem.lower()
				for t in self.bot.get_all_members():
					if str(t.id) == data[mem]['leader_id']:
						mem=t
						break
		for i in mem.roles:
			if i.name.lower().endswith("gym leader"):
				h=i.name.lower().split(" ")
				p=h[0]
				break
		
		if p==None:
			await ctx.send("Looks like you are not a gym leader")
			return
		if p not in data.keys():
			await ctx.send("Data Not Found! Ping Void")
		if data[p]['prem']=='0':
			await ctx.send("__```Leader Card```__"+f"``` Gym Name: {data[p]['gym_name']}\n\n Leader Name: {mem.name} \n\n Number of Battles: {data[p]['n_o_b']}\n\n Number of wins: {data[p]['n_o_w']}\n\n Balance: {data[p]['b']}```")
		else:
			colors=[1752220,3066993,3447003,10181046,15844367,15105570,1515833,9807270,8359053,3426654,1146986,2067276,2123412,7419530,12745742,11027200,10038562,9936031,12370112,2899536,16580705,
12320855]
			embed=discord.Embed(colour=random.choice(colors))
			embed.add_field(name="Leader Card",value=f" **Gym Name** : \n {data[p]['gym_name']}\n\n **Leader Name** : \n `{mem.name}`\n\n **Number of Battles** : \n{data[p]['n_o_b']}\n\n  **Number of wins** : \n{data[p]['n_o_w']}\n\n **Balance** : \n{data[p]['b']}") 
			await ctx.send(embed=embed)	
def setup(bot):
	bot.add_cog(leader_card(bot))
