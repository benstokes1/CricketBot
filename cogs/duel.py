import discord 
import asyncio
from discord.ext import commands
import json
class duel(commands.Cog):
	def __init__(self,bot):
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
			if h[0] not in data.keys():
				await ctx.send("Ping Void!")
			else:
				if data[h[0]]['b_c']=='3':
					await ctx.send("Gym is locked for now! Come after 12 hours")
					return
				elif data[h[0]]['b_c']=='2':
					
					data[h[0]]['n_o_b']=str(int(data[h[0]]['n_o_b']+1)
					data[h[0]]['n_o_w']=str(int(data[h[0]]['n_o_w']+1)
					data[h[0]]['b']=str(int(data[h[0]]['b']+100)
					data[h[0]]['b_c']=str(int(data[h[0]]['b_c'])+1)
					with open("./cogs/json/data.txt","w") as hh:
 						json.dump(data,hh)
					await asyncio.sleep(20)
					with open("./cogs/json/data.txt","r") as hh:
 						data=json.load(hh)
					with open("./cogs/json/data.txt","w") as hh:
 						json.dump(data,hh)
					data[h[0]]['b_c']='0'
							       
				else:
					data[h[0]['n_o_b']=str(int(data[h[0]]['n_o_b']+1)
					data[h[0]]['n_o_w']=str(int(data[h[0]]['n_o_w']+1)
					data[h[0]]['b']=str(int(data[h[0]]['b']+100)
					data[h[0]]['b_c']=str(int(data[h[0]]['b_c'])+1)
					with open("./cogs/json/data.txt","r") as hh:
 						json.dump(data,hh)
				
def setup(bot):
	bot.add_cog(duel(bot))
