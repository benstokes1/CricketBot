import discord 
import asyncio
import random 
from discord.ext import commands
class allow(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.Cog.listener()
	async def on_message(self,message):
		if message.content.startswith('?start'):
			channel = message.channel
			await channel.send('Whats ur name?')
			def check(m):
				k="void"
				return m.content.lower() == k and m.channel == channel
			msg = await self.bot.wait_for('message', check=check)
			await channel.send('Hello {.author}!'.format(msg))
		self.bot.process_commands(message)
	@commands.command()
	async def start(self,ctx):
		pass
def setup(bot):
	  bot.add_cog(allow(bot))
