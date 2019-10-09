import discord 
import asyncio
import random 
from discord.ext import commands


class reroll(commands.Cog):
	def __init__(self,bot):
		
		self.bot=bot
	@commands.command(aliases=["gd"])
	async def reroll(self,ctx,*,a=None):
		l=[]
		for q in ctx.message.guild.roles:
			if q.name.endswith("gym leader"):
				l.append(q.name)
		for i in l:
			g.append(i.split(" "))
			
		if ctx.message.author.guild_permissions.manage_roles or ctx.message.author.role.name in l:
			j=[]
			for q in ctx.message.guild.roles:
				if q.name.endswith("badge"):
					j.append(q)
			if a.lower()=="all":
				
				if ctx.message.author.guild_permissions.manage_roles:
					
					for q in self.bot.get_all_members:
						if q.role in j:
							await q.remove_roles(q.role,reason=ctx.message.author.name,atomic=True)
					await ctx.send(f"All the {q.role.name} have been stolen\nCheck Audit logs for more info")		
					return
							
				else:
					await ctx.send("```Syntax:b!reroll <name of gym>(ex: fire)(optional)```")
					return
			if a==None:
				for q in ctx.message.author.roles:
					if q.role.name in l:
						q=q.role.name.split(" ")
				for o in self.bot.get_all_members:
					for i in o.roles:
						p=i.name.split(" ")
						if p[0]==q[0]:
							await j.remove_roles(i.name,reason=ctx.message.author.name,atomic=True)
							break
				await ctx.send(f"All the {i.name}s have been stolen\nCheck Audit logs for more info")

			else:
				i=[]
				for q in g:
					i.append[q[0]]
				if a in i:
					for o in self.bot.get_all_members:
						for j in o.roles:
							p=i.name.split(" ")
							if p[0]==a:
								await j.remove_roles(i.name,reason=ctx.message.author.name,atomic=True)
								break
					await ctx.send(f"All the {i.name}s have been stolen\nCheck Audit logs for more info")
					
				else:
					
					

		if m==None:
			await ctx.send("```Syntax: b!gym_details <name of gym>(ex: fire)```")
			return 
		user=ctx.message
		m=m.lower()
		
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
						
						await ctx.send(f"``` {m} Leader: {leader} \n Last Battle: None\n\n Hall Of Fame: {trainer}```") 
						
					elif len(i.topic)==0:
						await ctx.send(f"``` {m} Leader: {leader} \n Last Battle: None\n\n Hall Of Fame: {trainer}```") 
					else:
						temp=i.topic.split("-")	
						if int(temp[1])!=t.id:
							await ctx.send(f"``` {m} Leader: {leader} \n Last Battle: None\n\n Hall Of Fame: {trainer}```") 
							return
						for f in self.bot.get_all_members():
							if f.id==int(temp[2]):
								break
						await ctx.send(f"``` {m} Leader: {leader} \n Last Battle: {t.name} vs {f.name}\n\n Hall Of Fame: {trainer}```") 
					break	
def setup(bot):
	bot.add_cog(reroll(bot))
