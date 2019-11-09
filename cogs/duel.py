import discord 
import asyncio
from discord.ext import commands
c=0
class duel(commands.Cog):
	def __init__(self,bot):
		global c
		self.bot=bot
	@commands.command(aliases=["sd"])
	async def start_duel(self,ctx,mem:discord.Member=None):
		l=[]
		rolez=None
		for q in ctx.message.guild.roles:
			if q.name.lower().endswith("gym leader"):
				l.append(q)
		for i in l:
			if i in ctx.message.author.roles:
				rolez=i
				break
		if rolez==None:
			await ctx.send(f"Looks like you are not a gym leader")
			return
		else:
			if mem==None:
				await ctx.send("```Syntax: b!sd <@mention>(trainer name)```")
				return
			await ctx.send(f"Good luck {mem.mention} uwu")
			h=rolez.name.lower().split(" ")
			with open("./cogs/json/data.txt","r") as hh:
				data=json.load(hh)
			if rolez[0] not in data.keys():
				await ctx.send("Ping Void!")
			else:
				if data[rolez[0]]['b_c']=='3':
					await ctx.send("Gym is locked for now! Come after 12 hours")
					return
				data[role[0]]['n_o_b']=str(int(data[role[0]]['n_o_b']+1)
				data[role[0]]['n_o_w']=str(int(data[role[0]]['n_o_w']+1)
				data[role[0]]['b']=str(int(data[role[0]]['b']+100)
				elif data[role[0]]['b_c']=='2':
					data[role[0]]['b_c']=str(int(data[role[0]]['b_c'])+1)

					await asyncio.sleep(20)
					data[role[0]]['b_c']='0'
				else:
					data[role[0]]['b_c']=str(int(data[role[0]]['b_c'])+1)
				
def setup(bot):
	bot.add_cog(duel(bot))
