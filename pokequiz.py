import discord 
import asyncio
import random 
from discord.ext import commands
import os
bot=commands.Bot(command_prefix='pepu ') 
@bot.event
async def on_ready():
	print("I am ready to serve ya")
@bot.command()
async def load(ctx,extension):
	for file in os.listdir("./cogs"):
		bot.load_extension("cogs."+filen+f"{extension}")
@bot.command()
async def unload(ctx,extension):
	for file in os.listdir("./cogs"):
		bot.unload_extension("cogs."+filen+f"{extension}")
for filename in os.listdir("./cogs"):
	for file in os.listdir("./cogs/"+filename):
		if file.endswith(".py"):
			bot.load_extension("cogs."+filename+f".{file[:-3]}")
@bot.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.CommandNotFound):
		await ctx.send("```This is not a command\nType ?help to see the list of commands```")

bot.run(os.getenv("BOT_TOKEN"))
