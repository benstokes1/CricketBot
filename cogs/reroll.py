import discord 
import asyncio
import random 
from discord.ext import commands


class reroll(commands.Cog):
	def __init__(self,bot):
		
		self.bot=bot
	@commands.command(aliases=["rr"])
	async def re_roll(self,ctx,*,a=None):
		l=[]
		g=[]
		for q in ctx.message.guild.roles:
			if q.name.endswith("gym leader"):
				l.append(q.name)
		for i in l:
			g.append(i.split(" "))
			print(g)
		print(l)
			
		if ctx.message.author.role.name in l:
			print(a)
			j=[]
			for q in ctx.message.guild.roles:
				if q.name.endswith("badge"):
					j.append(q)
			if a.lower()=="all":
				
				if ctx.message.author.guild_permissions.manage_roles:
					
					for q in self.bot.get_all_members:
						if q.role in j:
							await q.remove_roles(q.role,reason=ctx.message.author.name,atomic=True)
					await ctx.send(f"All the {q.role.name} have been stolen\nCheck Audit logs for more info")		
					return
							
				else:
					await ctx.send("```Syntax:b!re_roll <name of gym>(ex: fire)(optional)```")
					return
			if a==None:
				for q in ctx.message.author.roles:
					if q.role.name in l:
						q=q.role.name.split(" ")
				for o in self.bot.get_all_members:
					for i in o.roles:
						p=i.name.split(" ")
						if p[0]==q[0]:
							await o.remove_roles(i.name,reason=ctx.message.author.name,atomic=True)
							break
				await ctx.send(f"All the {i.name}s have been stolen\nCheck Audit logs for more info")

			else:
				i=[]
				for q in g:
					i.append[q[0]]
				if a in i:
					for o in self.bot.get_all_members:
						for j in o.roles:
							p=j.name.split(" ")
							if p[0]==a:
								await o.remove_roles(j.name,reason=ctx.message.author.name,atomic=True)
								break
					await ctx.send(f"All the {j.name}s have been stolen\nCheck Audit logs for more info")
					
				else:
					await ctx.send("```Syntax:b!reroll <name of gym>(ex: fire)(optional)```")
		else:
			await ctx.send("Looks like you arent any gym leeader")

		
def setup(bot):
	bot.add_cog(reroll(bot))
