import discord 
import asyncio
import random 
from discord.ext import commands

class clear(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	#clear
	@commands.command()
	async def clear(self,ctx,amount:int) :
		if ctx.channel.name.endswith("gym") or ctx.channel.name.startswith("gym")
			if role in ctx.messsage.author.roles:
				if amount>100:
					await ctx.send("```Enter a value <= 100```") 
				else:
					await ctx.channel.purge(limit=amount+1) 
					await ctx.send(f'Cleared {amount} messages')
					await asyncio.sleep(1)
					await ctx.channel.purge(limit=1)
			else:
				await ctx.send(f"{ctx.message.author.mention} Seems like you do not have perms to delete messages")
		else:
			await ctx.message("I am not able to clear the messages in this channel")
	@clear.error
	async def on_clear_error(self,ctx,error):
		if isinstance(error,commands.BadArgument):
			await ctx.send("```Please enter an integral amount of messages to be deleted```")
		if isinstance(error,commands.MissingRequiredArgument):
			await ctx.send("```Please enter the number of messsages to be deleted```")
				       
	
def setup(bot):
	bot.add_cog(clear(bot))
