import discord 
import asyncio
import random 
from discord.ext import commands


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
			if q.name.endswith("gym leader"):
				i=q.name.lower().split(" ")
				l.append(i[0])
		n=m
		m=n+" type gym"
		if m not in (l):
			await ctx.send("```Syntax: b!gym_details <name of gym>(ex: fire)```")
			return
		else:
			
			role = discord.utils.get(user.guild.roles,name=m+" leader")
			train= discord.utils.get(user.guild.roles,name=m+" badge")
			leader= ""
			trainer= ""
			for t in self.bot.get_all_members():
				if role in t.roles:
					leader+=" "+t.name+"\n"
					break
			for q in self.bot.get_all_members():
				if train in q.roles:
					trainer+=" "+q.name+"\n"
			p=m
			m=m.upper()+'\n\n'
			if leader=="":
				leader="None"
			if trainer=="":	
				trainer="None"
			else: 
				trainer="\n\n"+trainer+"\n"
		
			
			h=p.split(" ")
		
			for i in ctx.message.guild.text_channels:
				k=i.name.lower().split("-")
				if k[0]==h[0]:
				
					if i.topic==None:
						
						await ctx.send(f"``` {m} Leader: {leader} \n Total number of battles: 0 \n\n Last Battle: None\n\n Hall Of Fame: {trainer}```") 
						
					elif len(i.topic)==0:
						await ctx.send(f"``` {m} Leader: {leader} \n Total number of battles: 0 \n\n Last Battle: None\n\n Hall Of Fame: {trainer}```") 
					else:
						temp=i.topic.split("-")	
						if int(temp[1])!=t.id:
							await ctx.send(f"``` {m} Leader: {leader} \n Total number of battles: 0\n\n Last Battle: None\n\n Hall Of Fame: {trainer}```") 
							return
						for f in self.bot.get_all_members():
							if f.id==int(temp[2]):
								break
						await ctx.send(f"``` {m} Leader: {leader} \n Last Battle: {t.name} vs {f.name}\n\n Total number of battles: {temp[0]}\n\n Hall Of Fame: {trainer}```") 
					break	
def setup(bot):
	bot.add_cog(gym_details(bot))
