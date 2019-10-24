import discord 
import asyncio
import random 
from discord.ext import commands

class random(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	#clear
	@commands.command()
	async def random(self,ctx) :
		if ctx.message.author.guild_permissions.manage_messages:
		
			r=[]
			print("vnv")
			for q in self.bot.get_all_members():
				for ro in q.roles:
					if ro.name=="Tourney Participant":
						r.append(q.name)
			random.shuffle(r)
			print(r)
			le="P v P List"
			ke=""
			for i in range(len(r)):
				ke+=k[i]+"vs"+r[i+1]+"\n"
			le="```"+le+"```"
			ke="```"+ke+"```"
			await ctx.send(f"{le}\n{ke}")


					
		else:
			await ctx.send("Ayee!")
	
				       
	
def setup(bot):
	bot.add_cog(random(bot))
