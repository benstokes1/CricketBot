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
			await ctx.send("```Syntax: b!gym_details <name of gym (ex: fire type gym)>```")
			return 
		user=ctx.message
		m=m.lower()
		l=[]
		for q in self.bot.roles():
			if q.name.endswith("gym leader"):
				l.append(q.name)
		if m not in (l):
			await ctx.send("```Syntax: b!gym_details <name of gym (ex: fire type gym)>```")
			return
		else:
			role = discord.utils.get(user.guild.roles,name=m+" leader")
			train= discord.utils.get(user.guild.roles,name=m+" badge")
			leader= ""
			trainer= ""
			for q in self.bot.get_all_members():
				if role in q.roles:
					leader+=" "+q.name+"\n"
			for q in self.bot.get_all_members():
				if train in q.roles:
					trainer+=" "+q.name+"\n"
			m=m.upper()+'\n\n'
			leader="\n\n"+leader+"\n"
			trainer="\n\n"+trainer+"\n"
			await ctx.send(f"``` {m} Leader: {leader} Hall Of Fame: {trainer}```") 
def setup(bot):
	bot.add_cog(gym_details(bot))    
