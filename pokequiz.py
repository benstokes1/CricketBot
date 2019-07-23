import discord 
import asyncio
import random 
from discord.ext import commands
import os
import json
bot=commands.Bot(command_prefix='?')
bot.remove_command('help')
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
@bot.command()
async def help(ctx):
	await ctx.send("```HELP MENU:\nMy prefix is '?'\nCommands:\n?start: Starts the quiz \n?allow: Aloow the user to register for the quiz \n?register: Registers the user for the quiz\n```) 


bot.run(os.getenv("BOT_TOKEN"))
