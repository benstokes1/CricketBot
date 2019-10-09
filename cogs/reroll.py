import discord 
import asyncio
import random 
from discord.ext import commands


class reroll(commands.Cog):
	def __init__(self,bot):
		
		self.bot=bot
	@commands.command(aliases=["rr"])
	async def re_roll(self,ctx,*,a=None):
		if  role in l:
			
			j=[]
			for q in ctx.message.guild.roles:
				if q.name.endswith("badge"):
					j.append(q)
			
			if ctx.message.author.guild_permissions.manage_roles and a.lower()=="all":
				print("a")
				if ctx.message.author.guild_permissions.manage_roles:
					
					for q in self.bot.get_all_members:
						for i in range(len(j)):
							if q.role in i[0]:
								await q.remove_roles(q.role,reason=ctx.message.author.name,atomic=True)
					await ctx.send(f"All the {q.role.name} have been stolen\nCheck Audit logs for more info")		
					return
							
				else:
					await ctx.send("```Syntax:b!re_roll <name of gym>(ex: fire)(optional)```")
					return
			else:
				await ctx.send("Don't mess with me..`b!rr all` is the command..")
def setup(bot):
	bot.add_cog(reroll(bot))
