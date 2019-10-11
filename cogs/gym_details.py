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
			
			
			leader= ""
			trainer= ""
			for t in self.bot.get_all_members():
				for role in t.roles:
					if role.name.lower().endswith("gym leader"):
						i=role.naem.lower().split(" ")
						if m==i[0]:
							leader+=" "+t.name+"\n"
							break
						
			for q in self.bot.get_all_members():
				for role in q.roles:
					if role.name.lower().endswith("gym badge"):
						i=role.naem.lower().split(" ")
						if m==i[0]:
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
