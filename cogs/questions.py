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
			await channel.send('Whats the volution of pikachu?')
			def check(m):
				m=m.title()
				return m.content == "Raichu" 
			try:
				answer = await self.bot.wait_for('message', timeout=5.0, check=check)
			except asyncio.TimeoutError:
				await channel.send('Oops times up')
			else:
				await channel.send(f'Right answer {answer.author}')
	
	@commands.command()
	async def start(self,ctx):
		pass
def setup(bot):
	  bot.add_cog(start(bot))
