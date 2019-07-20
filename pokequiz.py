import discord 
import asyncio
import random 
from discord.ext import commands
import os
bot=commands.Bot(command_prefix='?') 
@bot.event
async def on_ready():
	print("Less go")
@bot.command()
async def load(ctx,extension):
	
	bot.load_extension(f"cogs.{extension}")
@bot.command()
async def unload(ctx,extension):
	
	bot.unload_extension(f"cogs.{extension}")
for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
			bot.load_extension(f"cogs.{filename[:-3]}")


bot.run(os.getenv("BOT_TOKEN"))
