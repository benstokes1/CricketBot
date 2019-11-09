import discord 
import asyncio
import random 
from discord.ext import commands

class clear(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.command()
	async def clear(self,ctx,amount=None) :
		if amount==None:
			await ctx.send("```Syntax: b!clear <amount>```")
		else:
			amount=int(amount)
			l=[]
			if ctx.message.channel.category.name=="«────── ☆GYMS☆ ──────»":
				for q in ctx.message.guild.roles:
					if q.name.lower().endswith("gym leader"):
						l.append(q)
				role=None
				for q in ctx.message.author.roles:
					if q in l:
						role=1
						break
				if  role or ctx.message.author.guild_permissions.manage_messages:
					if amount>100:
						await ctx.send("```Enter a value <= 100```") 
					else:
						await ctx.channel.purge(limit=amount+1) 
						await ctx.send(f'Cleared {amount} messages')
						await asyncio.sleep(0.2)
						await ctx.channel.purge(limit=1)
				else :
					await ctx.send(f"{ctx.message.author.mention} Seems like you do not have perms to delete messages")
			else:
				await ctx.send("I am not able to clear the messages in this channel")
	
				       
	
def setup(bot):
	bot.add_cog(clear(bot))
