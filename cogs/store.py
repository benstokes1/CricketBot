import discord 
import asyncio
from discord.ext import commands
class store(commands.Cog):
	def __init__(self,bot):
        	self.bot=bot
	@commands.command(aliases=["s"])
	async def store(self,ctx,*,m):
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
			if m==None:
				embed=discord.Embed(colour=3426654)
				embed.add_field(name="Store",value="\n\n1.`You want Pokecord Credits?`\n **100 pokecord credits** = 500 Gym Bot credits\n\n2.`Sick of posting the rules again and again?`\n **Custom Rules** = 1000 Gym Bot credits\n\n3.`Want to make your leader card fancy?`\n **Fancy Card** = 1500 Gym Bot credits\n\n4.`Dont have a Legendary Pokemon?`\n **Legendary/Mythical** = 3000 Gym Bot credits\n\n To buy an item type `b!store buy <number>`\n Example: `b!store buy 1` gives u 100 pokecord credits")
				await ctx.send(embed=embed) 
			elif 	
def setup(bot):
	bot.add_cog(store(bot))

