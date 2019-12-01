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
	async def start(self,ctx,t=None):
		channel=ctx.message.channel
		noww=datetime.now()
		if t==None:
			nex= noww+timedelta(minutes = 10)
		elif 's' in time.lower():
			t=int(t[:-1])
			nex= noww+timedelta(seconds = t)
		
		elif 'm' in time.lower():
			t=int(t[:-1])
			nex= noww+timedelta(minutes = t)
		
		elif 'h' in time.lower():
			t=int(t[:-1])
			nex= noww+timedelta(hours = t)
		
		elif 'd' in time.lower():
			t=int(t[:-1])
			nex= noww+timedelta(days = t)
		while 1:
			if noww==next:
				break
			else:
				await asyncio.sleep(0.5)
				await channel.send("Spam")
		
def setup(bot):
	bot.add_cog(start(bot))
