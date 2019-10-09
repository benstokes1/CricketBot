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
		print(l)
		if mem==None:
			print("g")
			mem=ctx.message.author
		else:
			if mem.lower() not in l:
				await ctx.send("```Syntax: b!leader_card <name of gym(ex: fire)>(optional if u are a gym leader)```")
				return
			else:
				mem=mem.lower()
				for t in self.bot.get_all_members():
					for i in t.roles:
						if i.name.lower() in l:
							mem=t
							break
		for i in mem.roles:
			print("i")
			if i.name.lower().endswith("gym leader"):
				h=i.name.lower.split(" ")
				print(h[0])
				p=h[0]
		print(p)
		if p==None:
			await ctx.send("Looks like you are not a gym leader")
			return
		for i in ctx.message.guild.text_channels:
			k=i.name.lower().split("-")
			print(k[0])
			if k[0]==p:
				if i.topic==None:
					await ctx.send("__```Leader Card```__"+f"``` Gym Name: {p} type gym\n\n Leader Name: {mem.name} \n\n Number of wins: 0\n\n Balance: 0```")
					break
				elif len(i.topic)==0:
					await ctx.send("__```Leader Card```__"+f"``` Gym Name: {p} typr gym\n\n Leader Name: {mem.name} \n\n Number of wins: 0\n\n Balance: 0```")
					break
				else:	
					temp=i.topic.split("-")
					if int(temp[1])!=ctx.message.author.id:
						await ctx.send("__```Leader Card```__"+f"``` Gym Name: {p} type gym\n\n Leader Name: {mem.name} \n\n Number of wins: 0\n\n Balance: 0```")
					else:
						count=1
						for q in ctx.message.guild.roles:
							if q.name.lower().endswith("gym badge"):
								k=q.name.split(" ")
								if p==k[0]:
									count+=1
						k=int(temp[0]-count)
						if k<0:
							await ctx.send("__```Leader Card```__"+f"``` Gym Name: {p} type gym\n\n Leader Name: {mem.name} \n\n Number of wins: 0\n\n Balance: 0```")	
						else:
							await ctx.send("__```Leader Card```__"+f"``` Gym Name: {p} type gym\n\n Leader Name: {mem.name} \n\n Number of wins: {k}\n\n Balance: {k*100}```")
				break
	
def setup(bot):
	bot.add_cog(leader_card(bot))
