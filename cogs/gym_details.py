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
			await ctx.send("```Syntax: g!gym_details <name of gym (ex: fire type gym```")
			return 
		user=ctx.message
		m=m.lower()
		l=["mixed type gym","dragon type gym","electric type gym","fire type gym","psychic type gym","grass type gym","dark type gym","mega gym gym","fighting type gym","rock type gym"]
		if m not in (l):
			await ctx.send("```Syntax: g!gym_details <name of gym (ex: fire type gym)>```")
			return
		else:
			role = discord.utils.get(user.guild.roles,name=m+" leader")
			train= discord.utils.get(user.guild.roles,name=m+" badge")
			leader= ""
			trainer= ""
			for q in self.bot.get_all_members():
				if role in q.roles:
					leader+=q.name+"\n"
			for q in self.bot.get_all_members():
				if train in q.roles:
					trainer+=q.name+"\n"
			m=m.upper()+'\n'
			leader="\n"+leader
			trainer="\n"+trainer
			await ctx.send(f"``` {m} Leader: {leader} Hall Of Fame: {trainer}```") 
def setup(bot):
	bot.add_cog(gym_details(bot))    
