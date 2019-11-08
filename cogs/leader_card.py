import discord 
import asyncio
from discord.ext import commands
class leader_card(commands.Cog):
	def __init__(self,bot):
		
		self.bot=bot
	@commands.command(aliases=["lc"])

	async def leader_card(self,ctx,mem=None):
		
		mem=mem.lower()
		l=[]
		p=None
		rolez=None
		for q in ctx.message.guild.roles:
			if q.name.lower().endswith("gym leader"):
				m=q.name.lower().split(" ")
				l.append(m[0])
		
		with open("./cogs/json/data.txt","r") as hh:
			data=json.load(hh)
		if mem==None:
			mem=ctx.message.author
		
		else:
			if mem.lower() not in l:
				await ctx.send("```Syntax: b!leader_card <name of gym(ex: fire)>(optional if u are a gym leader)```")
				return
			else:
				if mem not in data.keys():
					await ctx.send("Ping Void!")
					return
				for t in self.bot.get_all_members():
					if str(t.id) == data[mem]['leader_id']:
						mem=t
				
		for i in mem.roles:
			if i.name.lower().endswith("gym leader"):
				h=i.name.lower().split(" ")
				p=h[0]
		
		if p==None:
			await ctx.send("Looks like you are not a gym leader")
			return
		if data[p]['prem']=='0':
			await ctx.send("__```Leader Card```__"+f"``` Gym Name: {data[p]['gym_name']}\n\n Leader Name: {data[p]['leader_name']} \n\n Number of Battles: {data[p]['n_o_b']}\n\n Number of wins: {data[p]['n_o_w']}\n\n Balance: {data[p]['b']}```")
		else:
			embed=discord.Embed(colour=10181046)
			embed.add_field(name="Leader Card",value=f" **Gym Name** : \n {data[p]['gym_name']}\n\n **Leader Name** : \n `{data[p]['leader_name']}`\n\n Number of Battles: \n{data[p]['n_o_b']}\n\n  Number of wins: \n{data[p]['n_o_w']}\n\n Balance: \n{data[p]['b']}") 
				
def setup(bot):
	bot.add_cog(leader_card(bot))
