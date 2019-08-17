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
		
		if message.content.startswith('q!start'):
			role = discord.utils.get(message.guild.roles,name="quiz_master")
			rolez = discord.utils.get(message.guild.roles,name="registered")
			log=self.bot.get_channel(603358767643623427)
			channel = message.channel
			if role in message.author.roles:
				
				channel = message.channel
				await channel.send(f'{rolez.mention}\n```Each question has five choices. U need to type the answer (not the option number)```')
				await asyncio.sleep(10)
				
				with open("cogs/questions.txt","r") as question:
					question=list(question)
					q_no=0
					c_a=0
					h=0
					for i in question:
						q_no+=1
						multiplier=1
						if (c_a==0):
							h=random.choice([1,2,3,4])	
						i=i.split(':')
						for que in range(0,5):
							await channel.send(f"`{i[que]}`")
							await asyncio.sleep(1)
						if (c_a==h):
							multiplier=random.choice([2,3,4,5])
							await channel.send(f'`Woah a {multiplier}X popped in!!`\n`It got stuck to this question.....`')
							c_a=0
							
						answers=i[6][:-1]
						print(answers)
						
						def check(msg):
							return msg.content.title() == answers
						try:
							answer= await self.bot.wait_for('message', timeout=8.0, check=check)
						except asyncio.TimeoutError:
							await channel.send(f'Times up {rolez.mention}')
							c_a=0
							
							await channel.send('Get ready for the next question!! Go get your brains retards ..u guys have eight seconds of time')

							await log.send(f"No one from the {rolez.mention} got it right {role.mention}\n`Question: {i[0]}`\n`Answer: {answers}`\n`Reward: {multiplier*100}c`")
							await asyncio.sleep(8)
						else:
							await channel.send(f'Yay! right answer {answer.author.mention}')
							await log.send(f"{answer.author.mention} answered the {q_no} question {rolez.mention}\n`Question: {i[0]}`\n`Answer: {answers}`\n`Reward: {multiplier*100}c`")
							c_a+=1
							if q_no!=4:
								await channel.send('Get ready for the next question NOOBS!!')
								await asyncio.sleep(8)
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
		role = discord.utils.get(ctx.message.guild.roles,name="registered")
		
		registers=""
		
		for q in self.bot.get_all_members():
			
			if role in q.roles:
				registers+=q.name+"\n"
		registers="```"+registers+"```"
		await ctx.send(f'```The following have registered for the quiz```{registers}')
	@commands.command()
		
	async def reroll(self,ctx):
		role = discord.utils.get(ctx.message.guild.roles,name="quiz_master")
		roles=discord.utils.get(ctx.message.guild.roles,name="registered")
		if role in ctx.message.author.roles: 			
			for q in self.bot.get_all_members():
				if role in q.roles:
					await q.remove_roles(roles)
					await ctx.send("Uhh that was a very tough job!!! Good luck for the next Session")
		else:
			await ctx.send(f"{ctx.author.mention} YOU ARE NOT THE QUIZ MASTER NUB")
		
				
def setup(bot):
	bot.add_cog(start(bot))
