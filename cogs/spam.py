import discord 
import asyncio
import random 
from discord.ext import commands
import json
from datetime import datetime,timedelta
class start(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.command(aliases=["s"])
	async def start(self,ctx,time=None):
		channel=ctx.message.channel
		noww=datetime.now()
		if time==None:
			nex= now+timedelta(minutes = 10)
		elif 's' in time.lower():
			time=int(time[:-1])
			nex= now+timedelta(seconds = time)
		
		elif 'm' in time.lower():
			time=int(time[:-1])
			nex= now+timedelta(minutes = time)
		
		elif 'h' in time.lower():
			time=int(time[:-1])
			nex= now+timedelta(hours = time)
		
		elif 'd' in time.lower():
			time=int(time[:-1])
			nex= now+timedelta(days = time)
		while 1:
			if noww==next:
				break
			else:
				await channel.send("Spam")
		
def setup(bot):
	bot.add_cog(start(bot))
