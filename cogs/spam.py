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
	async def start(self,ctx,t=None,*,text=None):
		
		try:
			if type(int(t[:-1]))==int:
				try:
					if type(int(t))==int:
						text=t
						t=None
				except:
					
					if int(t[:-1]) >= 0:
						pass

					else:
						await ctx.send("Oops cant read negative numbers")
						return
		except:
			
			try:
				print(t)
				if type(int(t[3:len(t)-1]))==int:
					pass
			except:	
				if text==None:
					text=t
				else:
					text=t+" "+text
				t=None
			else:
				if t[:2]=="<@":
					if text==None:
						text=t

					else:
						text=t+" "+text
					t=None				
		for i in ctx.message.author.roles:
			if 'spam' in i.name.lower():
				
				channel=ctx.message.channel
				if text==None:
					text='Spam'
				noww=datetime.now()
				top=channel.topic
				await channel.edit(topic="stop :0")
				if t==None:
					while 1:
						if channel.topic=="stop :1":
							await channel.send("Processes stopped successfully")
							await channel.edit(topic=top)
							return
						noww=datetime.now()
						await asyncio.sleep(0.8)
						await channel.send(text)

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
						await channel.edit(topic=top)

						break
					else:
						if channel.topic=="stop :1":
							await channel.send("Processes stopped successfully")
							await channel.edit(topic=top)

							break
						noww=datetime.now()
						await asyncio.sleep(0.8)
						await channel.send(text)
				return
		await ctx.send("Looks like you dont have the spam role")

def setup(bot):
	bot.add_cog(start(bot))
