import discord 
import asyncio
from discord.ext import commands
class store(commands.Cog):
	def __init__(self,bot):
        	self.bot=bot
	@commands.command(aliases=["s"])
	async def store(self,ctx,*,m=None):
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
			print(m)

			rolez=rolez.name.lower().split(" ")

			if m==None:
				embed=discord.Embed(colour=3426654)
				embed.add_field(name="Store",value="\n\n1.`You want Pokecord Credits?`\n **100 pokecord credits** = 500 Gym Bot credits\n\n2.`Sick of posting the rules again and again?`\n **Custom Rules** = 1000 Gym Bot credits\n\n3.`Want to make your leader card fancy?`\n **Fancy Card** = 1500 Gym Bot credits\n\n4.`Dont have a Legendary Pokemon?`\n **Legendary/Mythical** = 3000 Gym Bot credits\n\n To buy an item type `b!store buy <number>`\n Example: `b!store buy 1` gives u 100 pokecord credits")
				await ctx.send(embed=embed) 
			elif m.lower() not in ['buy 1','buy 2','buy 3','buy 4']:
				await ctx.send("Beep-boop! Item not found")
			else:
				m=m.split(" ")
				m=m[2]
				with open("./cogs/json/data.json","r") as hh:
					data=json.load(hh)
				if rolez[0] not in data.keys():
					await ctx.send("Ping Void!")
					return
				if m==1:
					k=int(data[rolez[0]]['b'])
					if k<500:
						await ctx.send("You cant afford to buy this")
					else:
						data[rolez[0]]['b']=str(k-500)
						await ctx.send("You have succesfully bought the credits! Claim from Void!")
				elif m==2:
					
					k=int(data[rolez[0]]['b'])
					if k<1000:
						await ctx.send("You cant afford to buy this")
					else:
						data[rolez[0]]['b']=str(k-1000)
						await ctx.send("You have succesfully bought the Custom Rules! Claim from Void!")
				elif m==3:
					
					k=int(data[rolez[0]]['b'])
					if k<1500:
						await ctx.send("You cant afford to buy this")
					else:
						data[rolez[0]]['b']=str(k-1500)
						data[rolez[0]]['prem']='1'
						await ctx.send("You have succesfully bought the Fancy Card! Claim from Void!")
				else:
					
					k=int(data[rolez[0]]['b'])
					if k<3000:
						await ctx.send("You cant afford to buy this")
					else:
						data[rolez[0]]['b']=str(k-3000)
						await ctx.send("You have succesfully bought the Legendary! Claim from Void!")
				
				with open("./cogs/json/data.json","w") as hh:
					json.dump(data)
				
					
def setup(bot):
	bot.add_cog(store(bot))

