import discord 
import asyncio
import random 
from discord.ext import commands
class start(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.Cog.listener()
	async def on_message(self,message):
		if message.content.startswith('?start'):
			channel = message.channel
			await channel.send('Select a category')
			await channel.send('1.Fire\n2.Water')
			def check(m):
				return m.content.title() 
			answer = await self.bot.wait_for('message',check=check)
			await channel.send(f'{answer.content} {answer.author.mention}')
	
	@commands.command()
	async def start(self,ctx):
		pass
def setup(bot):
	  bot.add_cog(start(bot))
