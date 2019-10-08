import discord 
import asyncio
import random 
from discord.ext import commands

class clear(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	#clear
	@commands.command()
	async def clear(self,ctx,amount=None) :
		if amount==None:
			await ctx.send("```Syntax: b!clear <amount>```")
		else:
			amount=int(amount)
			if ctx.message.channel.category.name.lower=="gyms":
				role = discord.utils.get(ctx.message.guild.roles,name="gym leaders")
				if role in ctx.message.author.roles or ctx.message.author.guild_permissions.manage_messages:
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
