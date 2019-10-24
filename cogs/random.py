import discord 
import asyncio
import random 
from discord.ext import commands

class random(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	#clear
	@commands.command()
	async def random(self,ctx,mem:discord.Member=None) :
		if ctx.message.author.guild_permissions.manage_messages:
			
			if mem==None:
				await ctx.send("```Syntax: b!random <@```")
			else:
				r=[]
				for q in self.bot.get_all_members():
					for role in q.roles:
						if role.name.lower()=="tourney participant":
							r.append(q.name)
				print(r)
				i=1
				k=[r[0]]
				while i<len(r):
					h=random.choice(r)
					if h in k:
						continue
					else:
						k.append(h)
						i+=1
				le="P v P List"
				ke=""
				for i in range(len(k)):
					le+=k[i]+"vs"+k[i+1]+"\n"
				le="```"+le+"```"
				ke="```"+ke+"```"
				await ctx.send(f"{le}\n{ke}")
					
						
					
		else:
			await ctx.send("Ayee!")
	
				       
	
def setup(bot):
	bot.add_cog(random(bot))
