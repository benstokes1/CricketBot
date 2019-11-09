import discord 
import asyncio
import random 
from discord.ext import commands
import json
class trainer_card(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.command(aliases=["tc"])
	async def trainer_card(self,ctx,names:discord.Member=None):
		badges=[]
		s=""
		with open("./cogs/json/data.json","r") as hh:
			data=json.load(hh)
		if names == None:
			names = ctx.message.author
		for i in data.keys():
			if str(names.id) in data[i]['h_o_f_i']:
				i=i.title()+" Badge"
				badges.append(i)
		embed=discord.Embed(colour=15844367)
		if len(badges)==0:
			embed.add_field(name="Trainer Card",value=f" **Trainer Name** :\n `{names.name}` \n\n **Number of Badges** :\n {0}\n\n **Gyms Defeated** :\n None") 
			await ctx.send(embed = embed)
		else:
			for i in badges:
				s+="\n"+" "+i	
			s="\n"+s
			embed.add_field(name="Trainer Card",value=f" **Trainer Name** :\n `{names.name}` \n\n **Number of Badges** :\n {len(badges)}\n\n **Gyms Defeated** : {s}") 
			await ctx.send(embed = embed)
def setup(bot):
	bot.add_cog(trainer_card(bot))
