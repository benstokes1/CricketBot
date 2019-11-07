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
			
			
			leader= ""
			trainer= ""
			for t in self.bot.get_all_members():
				for role in t.roles:
					if role.name.lower().endswith("gym leader"):
						i=role.name.lower().split(" ")
						if n==i[0]:
							leader+=t.name+"\n"
							train=t
							break
			for q in self.bot.get_all_members():
				for role in q.roles:
					if role.name.lower().endswith("gym badge"):
						i=role.name.lower().split(" ")
						if n==i[0]:
							trainer+=" "+q.name+"\n"
							break
			p=m
			m=m.upper()+'\n\n'
			if leader=="":
				leader="None"
			if trainer=="":	
				trainer="None"
			else: 
				trainer="\n\n"+trainer+"\n"
		
			
			with open("cogs.json.data.txt","r") as hh:
				data=json.load(hh)
			print("bh")
			for i in l:
				if i in data:
					for t in self.bot.get_all_members():
						if str(t.id)==data[i][leader_id]:
							hm=t.name
			if data[i][l_b]=="0":
				return
			for i in l:
				if i in data:
					for t in self.bot.get_all_members():
						if str(t.id)==data[i][l_b]:
							hs=t.name
			await ctx.send(f"``` {m} Leader: {hm} \n Total number of battles: {data[i][n_o_b]} \n\n Last Battle: {hm} vs {hs}\n\n Hall Of Fame: {trainer}```") 
			for i in ctx.message.guild.text_channels:
				k=i.name.lower().split("-")
				print(k[0])
				if n in k[0]:
				
					if i.topic==None:
						await ctx.send(f"``` {m} Leader: {leader} \n Total number of battles: 0 \n\n Last Battle: None\n\n Hall Of Fame: {trainer}```") 
						
					elif len(i.topic)==0:
						await ctx.send(f"``` {m} Leader: {leader} \n Total number of battles: 0 \n\n Last Battle: None\n\n Hall Of Fame: {trainer}```") 
					else:
						temp=i.topic.split("-")	
						if int(temp[1])!=train.id:
							print("O")
							await ctx.send(f"``` {m} Leader: {leader} \n Total number of battles: 0\n\n Last Battle: None\n\n Hall Of Fame: {trainer}```") 
							return
						for f in self.bot.get_all_members():
							if f.id==int(temp[2]):
								break
						await ctx.send(f"``` {m} Leader: {leader} \n Last Battle: {train.name} vs {f.name}\n\n Total number of battles: {temp[0]}\n\n Hall Of Fame: {trainer}```") 
					break	
def setup(bot):
	bot.add_cog(gym_details(bot))
