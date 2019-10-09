import discord 
import asyncio
import random 
from discord.ext import commands


class reroll(commands.Cog):
	def __init__(self,bot):
		
		self.bot=bot
	@commands.command(aliases=["rr"])
	async def re_roll(self,ctx,*,a=None):
		if a==None:
			await ctx.send("```Syntax:b!re_roll <name of gym>(ex: fire)(optional)```")

		j=[]
		for q in ctx.message.guild.roles:
				if q.name.lower().endswith("badge"):
					j.append(q.name)
		if ctx.message.author.guild_permissions.manage_roles:
			if a.lower()=="all":
				print("a")
				if ctx.message.author.guild_permissions.manage_roles:
					for q in self.bot.get_all_members:
						print("j")
						for i in q.roles:
							if i.name in j:
								print("O")
								await q.remove_roles(q.role,reason=ctx.message.author.name,atomic=True)
					await ctx.send(f"All the badges have been stolen\nCheck Audit logs for more info")		
					return
							
				else:
					await ctx.send("```Syntax:b!re_roll <name of gym>(ex: fire)(optional)```")
					return
			else:
				await ctx.send("Arghhhh...Don't mess with me..`b!rr all` is the command..")
		else:
			await ctx.send("Looks like you aint a leader")
def setup(bot):
	bot.add_cog(reroll(bot))
