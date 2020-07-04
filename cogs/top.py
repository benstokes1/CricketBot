import discord 
import asyncio
from discord.ext import commands
import json
class top(commands.Cog):
	def __init__(self,bot):
        	self.bot=bot
	@commands.command()
	async def top(self,ctx,*,m=None):
		x=db_collectio.find().sort([("won",-1)("winning_percentage",-1)])
		top_players=[]
		if m.lower()=="server":
			for j in x:
				if len(top_players)==5:
					break
				for i in ctx.message.guild.members:
					if i.id==j["id"]:
						top_players.append(i.name)
						break
			p=""
			for i in top_players:
				p+=str(i+1)+". "+i+"\n"	
			embed=discord.Embed(title="Top players",description=p)
			await ctx.send(embed=embed)
		elif m.lower()=="global":
			for j in x:
				if len(top_player)==5:
					break
				i=await self.bot.fetch_member(j["id"])
				if i==None:
					pass
				else:
					top_player.append[i.name]
			p=""
			for i in top_players:
				p+=str(i+1)+". "+i+"\n"	
			embed=discord.Embed(title="Top players",description=p)
			await ctx.send(embed=embed)
def setup(bot):
	bot.add_cog(top(bot))
