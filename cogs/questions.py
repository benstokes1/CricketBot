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
			while 1:
				answer = await self.bot.wait_for('message')
				if answer.content.title() in ["Fire","Water"]:
					await channel.send(f'{answer.content} {answer.author.mention}')
					break
				else:
					await channel.send('Noob head type a right option')
					continue
			with open("cogs/Fire.txt","r") as question:
				for i in question:
					i=i.split(':')
					await channel.send(i[0])
					def check(m):
						return m.content.title()==i[1]
					try:
						answer = await self.bot.wait_for('message',timeout=10,check=check)
					except asyncio.TimeoutError:
						await channel.send("Time's up :cry:")
					else:
						await channel.send("Right answer")
					
						
					
				
	
	@commands.command()
	async def start(self,ctx):
		pass
def setup(bot):
	  bot.add_cog(start(bot))
