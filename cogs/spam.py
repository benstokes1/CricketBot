import discord 
import asyncio
import random 
from discord.ext import commands
import json
from datetime import datetime,timedelta
class start(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.command()
	async def start(self,ctx,t=None):
		channel=ctx.message.channel
		noww=datetime.now()
		channel.edit(topic="stop :0")
		await channel.edit(topic="stop :0")
		if t==None:
			while 1:
				if channel.topic=="stop :1":
					await channel.send("Processes stopped successfully")
					break
				noww=datetime.now()
				await asyncio.sleep(0.8)
				await channel.send("Spam")
			return
		elif 's' in t.lower():
			t=int(t[:-1])
			print(t)
			nex= noww+timedelta(seconds = t)
			print(nex)
			print(noww)
		
		elif 'm' in t.lower():
			t=int(t[:-1])
			nex= noww+timedelta(minutes = t)
		
		elif 'h' in t.lower():
			t=int(t[:-1])
			nex= noww+timedelta(hours = t)
		
		elif 'd' in t.lower():
			t=int(t[:-1])
			nex= noww+timedelta(days = t)
		
		while 1:
			if noww>=nex:
				break
			else:
				if channel.topic=="stop :1":
					await channel.send("Processes stopped successfully")
					break
				noww=datetime.now()
				await asyncio.sleep(0.8)
				await channel.send("Spam")
		
def setup(bot):
	bot.add_cog(start(bot))
