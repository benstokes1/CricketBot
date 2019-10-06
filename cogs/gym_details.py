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
		m.lower()
		l=["mixed type gym leader","dragon type gym leader","electric type gym leader","fire type gym leader","psychic type gym leader","grass type gym Leader","dark type gym leader","mega gym gym leader","fighting type gym leader","rock type gym leader"]
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
			await ctx.send(f"```` {m.upper()+"\n"} Leader: {leader} Hall Of Fame: {trainer}```") 
def setup(bot):
	bot.add_cog(gym_details(bot))    
