import discord 
import asyncio
from discord.ext import commands
class leader_card(commands.Cog):
	def __init__(self,bot):
		
		self.bot=bot
	@commands.command(aliases=["lc"])

	async def leader_card(self,ctx,*,mem=None):
		
	
		l=[]
		p=None
		rolez=None
		for q in ctx.message.guild.roles:
			if q.name.lower().endswith("gym leader"):
				m=q.name.lower().split(" ")
				l.append(m[0])
		
		if mem==None:
			
			mem=ctx.message.author
		else:
			if mem.lower() not in l:
				await ctx.send("```Syntax: b!leader_card <name of gym(ex: fire)>(optional if u are a gym leader)```")
				return
			else:
				mem=mem.lower()
				for t in self.bot.get_all_members():
					for i in t.roles:
						if i.name.lower().endswith("gym leader"): 
							g=i.name.lower().split(" ")
							if g[0] == mem:
								mem=t
								break
		for i in mem.roles:
			if i.name.lower().endswith("gym leader"):
				h=i.name.lower().split(" ")
				p=h[0]
		
		if p==None:
			await ctx.send("Looks like you are not a gym leader")
			return
		for i in ctx.message.guild.text_channels:
			k=i.name.lower().split("-")
			
			if k[0]==p:
				
				p=p.title()
				
				if i.topic==None:
					await ctx.send("__```Leader Card```__"+f"``` Gym Name: {p} type gym\n\n Leader Name: {mem.name} \n\n Number of Battles: 0\n\n Number of wins: 0\n\n Balance: 0```")
					break
				elif len(i.topic)==0:
					await ctx.send("__```Leader Card```__"+f"``` Gym Name: {p} typr gym\n\n Leader Name: {mem.name} \n\n Number of Battles: 0\n\n Number of wins: 0\n\n Balance: 0```")
					break
				else:	
					temp=i.topic.split("-")
					if int(temp[1])!=mem.id:
						await ctx.send("__```Leader Card```__"+f"``` Gym Name: {p} type gym\n\n Leader Name: {mem.name} \n\n Number of Battles: 0\n\n Number of wins: 0\n\n Balance: 0```")
					else:
						count=0
						for t in self.bot.get_all_members():
							for q in t.roles:
								if q.name.lower().endswith("gym badge"):
									k=q.name.lower().split(" ")
							
									if p==k[0].title():
										count+=1
						print(count)
						k=int(temp[0])-count
						if k<0:
							print(k)
							await ctx.send("__```Leader Card```__"+f"``` Gym Name: {p} type gym\n\n Leader Name: {mem.name} \n\n Number of Battles: 0\n\n Number of wins: 0\n\n Balance: 0```")	
						else:
							print(k)
							await ctx.send("__```Leader Card```__"+f"``` Gym Name: {p} type gym\n\n Leader Name: {mem.name} \n\n Number of Battles: {temp[0]}\n\n Number of wins: {k}\n\n Balance: {k*100}```")
				break
	
def setup(bot):
	bot.add_cog(leader_card(bot))
