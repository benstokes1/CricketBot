import discord 
import asyncio
import random 
from discord.ext import commands

class start(commands.Cog):
	def __init__(self,bot):
		global log
		self.bot=bot
		
	@commands.Cog.listener()
	async def on_message(self,message):
		role = discord.utils.get(message.guild.roles,name="quiz_master")
		rolez = discord.utils.get(message.guild.roles,name="registered")
		log=self.bot.get_channel(603358767643623427)
		channel = message.channel
		if message.content.startswith('~start'):	
			if role in message.author.roles:
				
				channel = message.channel
				await channel.send(f'{rolez.mention} GET READY FOR THE QUIZ!')
				await asyncio.sleep(10)
				
				with open("cogs/questions.txt","r") as question:
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
							await channel.send(f'Woah a {multiplier}X popped in!!\nIt got stuck to this question.....')
							c_a=0
							
						answers=i[1][:-1]
						
						def check(msg):
							return msg.content.title() == answers
						try:
							answer= await self.bot.wait_for('message', timeout=10.0, check=check)
						except asyncio.TimeoutError:
							await channel.send(f'Times up {rolez.mention}')
							c_a=0
							
							await channel.send('Get ready for the next question!! Go get your brains ..u guys have five seconds of time')

							await log.send(f"No one from the {rolez.mention} got it right {role.mention}\n`Answer: {answers}`\n`reward: {multiplier*100}c`")
							await asyncio.sleep(5)
						else:
							await channel.send(f'Yay! right answer {answer.author.mention}')
							await log.send(f"{answer.author.mention} answered the {q_no} question {rolez.mention}\n`Answer: {answers}`\n`reward: {multiplier*100}c`")
							c_a+=1
							if q_no!=10:
								await channel.send('Get ready for the next question NOOBS!! Lets take a break for 5s')
								await asyncio.sleep(5)
							else:
								await channel.send(f'GG! We are done with the quiz! Winners claim your rewards from {role.mention}')
								await log.send(f'GG! We are done with the quiz! Winners claim your rewards from {role.mention}')
			else:
				await channel.send("Seems like u dont have the pokequiz-master role")
					
						
					
				
	
	@commands.command()
	async def start(self,ctx):
		pass
	@commands.command(aliases=["p"])
	async def participants(self,ctx):
		role = discord.utils.get(ctx.message.guild.roles,name="quiz_master")
		
		registers=""
		print(self.bot.get_all_members)
		for q in self.bot.get_all_members:
			if role in q.roles:
				registers+=i.name+"\n"
		registers="```"+resgisters+"```"
		await ctx.send(registers)
def setup(bot):
	bot.add_cog(start(bot))
