import discord 
import asyncio
import random 
from discord.ext import commands
log=0
class start(commands.Cog):
	def __init__(self,bot):
		global log
		
		
		self.bot=bot
		log=self.bot.get_channel(603358767643623427)
	@commands.Cog.listener()
	async def on_message(self,message):
		role = discord.utils.get(message.guild.roles,name="quiz_master")
		rolez = discord.utils.get(message.guild.roles,name="registered")
		channel = message.channel
		if message.content.startswith('?start'):	
			if role in message.author.roles:
				
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
					q_no=0
					for i in question:
						q_no+=1
						multiplier=1
						c_a=0
						i=i.split(':')
						await channel.send(i[0])
						if (c_a==3):
							multiplier=random.random([2,3,4,5,6,7,8,9,10])
							c_a=0
						answer=i[1][:-1]
						await channel.send(f'Woah a {multiplier}X popped in!!\nIt got stuck to this question.....')
						def check(msg):
							return msg.content.title() == answer
						try:
							answer= await self.bot.wait_for('message', timeout=10.0, check=check)
						except asyncio.TimeoutError:
							await channel.send(f'Times up {rolez.mention}')
							c_a=0
							await channel.send('Get ready for the next question NOOBS!! Lets take a break for 5s')
						else:
							await channel.send(f'Yay! right answer {message.author.mention}')
							await log.send(f"{message.author.mention} answered the {q_no} question {rolez.mention}\n`Answer: {answer}`\n`reward: {multiplier*100}c")
							c_a+=1
							if q_no!=10:
								await channel.send('Get ready for the next question~!! Lets take a break for 5s')
							else:
								await channel.send(f'GG! We are done with the quiz! Winners claim your rewards from {role.mention}')
			else:
				await channel.send("Seems like u dont have the pokequiz-master role")
					
						
					
				
	
	@commands.command()
	async def start(self,ctx):
		pass
	@commands.command()
	async def log(self,ctx):
		await ctx.send(f"{ctx.message.channel.id}")
def setup(bot):
	bot.add_cog(start(bot))
