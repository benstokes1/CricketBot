import discord 
import asyncio
import random 
from discord.ext import commands
import json

class gym_details(commands.Cog):
	def __init__(self,bot):
		
		self.bot=bot
	@commands.command(aliases=["gd"])
	async def gym_details(self,ctx,*,m=None):
		if m==None:
			await ctx.send("```Syntax: b!gym_details <name of gym>(ex: fire)```")
			return 
		user=ctx.message
		m=m.lower()
		l=[]
		for q in ctx.message.guild.roles:
			if q.name.lower().endswith("gym leader"):
				i=q.name.lower().split(" ")
				l.append(i[0])
		n=m
		m=n+" type gym"
		if n not in (l):
			await ctx.send("```Syntax: b!gym_details <name of gym>(ex: fire)```")
			return
		else:
			
			
			trainer= ""
			
			for q in self.bot.get_all_members():
				for role in q.roles:
					if role.name.lower().endswith("gym badge"):
						i=role.name.lower().split(" ")
						if n==i[0]:
							trainer+=" "+q.name+"\n"
							break
			
			if trainer=="":	
				trainer="None"
			else: 
				trainer="\n\n"+trainer+"\n"
		
			
			with open("./cogs/json/data.txt","r") as hh:
				data=json.load(hh)
			hm=None
			if n in data.keys():
				for t in self.bot.get_all_members():
					if str(t.id)==data[n]["leader_id"]:
						hm=t.name
						break
				
			if hm==None:
				await ctx.send(f"No {data[n]['gym_name']} leader")
				return
			hs=None
			if n in data.keys():
				for t in self.bot.get_all_members():
					if str(t.id)==data[n]["l_b"]:
						hs=t.name
						break
			if hm==None:
				await ctx.send(f"__```{data[n]['gym_name']}```__"+"``` Leader: {hm} \n\n Total number of battles: '0' \n\n Last Battle: 'None'\n\n Hall Of Fame: 'None'```") 
				return
			await ctx.send(f"__```{data[n]['gym_name']}```__"+"``` Leader: {hm} \n\n Total number of battles: {data[n]['n_o_b']} \n\n Last Battle: {hm} vs {hs}\n\n Hall Of Fame: {trainer}```") 
				
def setup(bot):
	bot.add_cog(gym_details(bot))
