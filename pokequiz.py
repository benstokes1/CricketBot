import discord 
import asyncio
import random
from discord.ext import commands
import os
import json
bot=commands.Bot(command_prefix='g!')
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
	await ctx.send("```HELP MENU:\n\nMy prefix is 'g!'\n\nCommands:\n\ng!gym_details <name of gym>:  Gives gym details\n\ng!give_badge <@mention>: Gives the mentioned user badge\n\ng!gym_leaders: Gives the list of gym leaders\n\ng!clear <number>: Clears the messages```") 


bot.run(os.getenv("BOT_TOKEN"))
