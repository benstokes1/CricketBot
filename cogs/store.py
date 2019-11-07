import discord 
import asyncio
from discord.ext import commands
c=0
class store(commands.Cog):
	def __init__(self,bot):
		global c
		self.bot=bot
	@commands.command(aliases=["s"])

	async def store(self,ctx):
		
		
		l=[]
		rolez=None
		for q in ctx.message.guild.roles:
			if q.name.lower().endswith("gym leader"):
				l.append(q)
		for i in l:
			if i in ctx.message.author.roles:
				rolez=i
				break
		if rolez==None:
			await ctx.send(f"Looks like you are not a gym leader")
			return
		else:
      			embed=discord.Embed(colour=discord.Color.red())

      			embed.add_field(name="Store",value="\n\n You want Pokecord Credits?\n 100 pokecord credits = 500 Gym Bot credits\n\n Sick of posting the rules again and again?\n Custom Rules = 1000 Gym Bot credits\n\n Want to make your leader card fancy?\n fancy Card = 1500 Gym Bot credits\n\n Dont have a Legendary Pokemon?\n Legendary?Mythical = 3000 credits ") 

def setup(bot):
	bot.add_cog(store(bot))
