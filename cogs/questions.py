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
				option = await self.bot.wait_for('message')
				if option.content.title() in ["Fire","Water"]:
					await channel.send(f'{option.content} {option.author.mention}')
					break
				else:
					await channel.send('Noob head type a right option')
					continue
			with open("cogs/"+option.content.title()+".txt","r") as question:
				question=list(question)
				for i in question:
					i=i.split(':')
					list=[]
					await channel.send(i[0])
					def check(msg):
						list=list.append(i[1][:-2])
						print(list)
						return msg.content.title() == i[1][:-2]
					try:
            					answer= await self.bot.wait_for('message', timeout=10.0, check=check)
					except asyncio.TimeoutError:
						await channel.send('Times up')
					else:
						await channel.send('Right answer')
					
						
					
				
	
	@commands.command()
	async def start(self,ctx):
		pass
def setup(bot):
	  bot.add_cog(start(bot))
