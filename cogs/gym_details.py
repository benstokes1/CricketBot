import discord 
import asyncio
import random 
from discord.ext import commands
import json

class gym_details(commands.Cog):
	def __init__(self,bot):
		
		self.bot=bot
	@commands.command(aliases=["gd"])
	async def gym_details(self,ctx,*,n=None):
		if n==None:
			await ctx.send("```Syntax: b!gym_details <name of gym>(ex: fire)```")
			return 
		user=ctx.message
		n=n.lower()
		l=[]
		for q in ctx.message.guild.roles:
			if q.name.lower().endswith("gym leader"):
				i=q.name.lower().split(" ")
				l.append(i[0])
		if n not in (l):
			await ctx.send("```Syntax: b!gym_details <name of gym>(ex: fire)```")
			return
		else:
			with open("./cogs/json/data.txt","r") as hh:
				data=json.load(hh)
			trainers=""
			hm=None

			if n in data.keys():
				for t in self.bot.get_all_members():
					if str(t.id)==data[n]["leader_id"]:
						hm=t.name
						break
			if n not in data.keys():
				await ctx.send(f"No data related to {n.lower()} type gym")
				return 
			if type(data[n]["h_o_f"]) == str :
				trainers=" `None`"
			for i in data[n]["h_o_f"]:
				trainers+=" "+"`"+i+"`"+"\n"
			if hm==None:
				await ctx.send(f"No {data[n]['gym_name']} leader")
				return
			hs=None
			if n in data.keys():
				for t in self.bot.get_all_members():
					if str(t.id)==data[n]["l_b"]:
						hs=t.name
						break
		
			embed=discord.Embed(colour=10181046)
			if hs==None:
				embed.add_field(name="Gym Details",value=f" **Gym Name** : {data[n]['gym_name']}\n\n **Leader** : {hm}\n\n **Total number of battles** : {data[n]['n_o_b']}\n\n **Last Battle** : None\n\n **Hall Of Fame** : \n{trainers}")
				await ctx.send(embed=embed) 
				return
			embed.add_field(name="Gym Details",value=f" **Gym Name** : {data[n]['gym_name']}\n\n **Leader** : {hm}\n\n **Total number of battles** : {data[n]['n_o_b']}\n\n **Last Battle** : {hm} vs {hs}\n\n **Hall Of Fame** :\n{trainers}")
			
			await ctx.send(embed=embed)				
def setup(bot):
	bot.add_cog(gym_details(bot))
