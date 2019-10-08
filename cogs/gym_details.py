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
				l.append(q.name[:-7])
		m+=" type gym"
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
			leader="\n\n"+leader+"\n"
			trainer="\n\n"+trainer+"\n"
			h=p.split(" ")
			print(h)
			for i in ctx.message.guild.text_channels:
				k=i.name.lower().split("-")
				if k[0]==h[0]:
					print(k)
					if i.topic=="":
						await ctx.send(f"``` {m} Leader: {leader} \n Last Battle: None\n\n Hall Of Fame: {trainer}```") 
						return
					else:
						temp=i.topic.split("-")
						if temp[1]!=t.name:
							await ctx.send(f"``` {m} Leader: {leader} \n Last Battle: None\n\n Hall Of Fame: {trainer}```") 
							return
						await ctx.send(f"``` {m} Leader: {leader} \n\n Last Battle: {temp[1]} vs {temp[2]}\n Hall Of Fame: {trainer}```") 
					break	
def setup(bot):
	bot.add_cog(gym_details(bot))    
