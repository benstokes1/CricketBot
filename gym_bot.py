import discord 
import asyncio
import random
from discord.ext import commands
import os
import json
bot=commands.Bot(command_prefix='b!')
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
	await ctx.send("```HELP MENU:\n\nMy prefix is 'b!'\n\nCommands:\n\nb!gym_details <name of gym>:  Gives gym details\n\nb!give_badge <@mention>: Gives the mentioned user badge\n\nb!gym_leaders: Gives the list of gym leaders\n\nb!clear <number>: Clears the messages\n\nb!show_badges <@mention>(optional) : Shows the badges owned by the trainer```") 
@bot.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.CommandNotFound):
		await ctx.send("```This is not a command\n\nType b!help to see the list of commands```")

bot.run(os.getenv("BOT_TOKEN"))
