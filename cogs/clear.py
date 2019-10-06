import discord 
import asyncio
import random 
from discord.ext import commands
welcome_channel=None
welcome_message=None
goodbye_channel=None
goodbye_channel=None
class clear(commands.Cog):
	def __init__(self,bot):
		global welcome_channel
		self.bot=bot
	#clear
	@commands.command()
	async def clear(self,ctx,amount:int) :
		if ctx.message.author.guild_permissions.manage_messages:
			if amount>300:
				await ctx.send("```Enter a value <= 300```") 
			else:
				await ctx.channel.purge(limit=amount+1) 
				await ctx.send(f'Cleared {amount} messages')
				await asyncio.sleep(2)
				await ctx.channel.purge(limit=1)
		else:
			await ctx.send(f"{ctx.message.author.mention} Seems like you do not have perms to manage messages")
	@clear.error
	async def on_clear_error(self,ctx,error):
		if isinstance(error,commands.BadArgument):
			await ctx.send("```Please enter an integral amount of messages to be deleted```")
		if isinstance(error,commands.MissingRequiredArgument):
			await ctx.send("```Please enter the number of messsages to be deleted```")
				       
	
def setup(bot):
	bot.add_cog(clear(bot))
