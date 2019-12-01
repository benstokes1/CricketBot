import discord 
import asyncio
import random
from discord.ext import commands
import os
import json
bot=commands.Bot(command_prefix='s!')
bot.remove_command('help')
@bot.event
async def on_ready():
	print("Less go")
@bot.command()
async def load(ctx,extension):
	
	bot.load_extension(f"cogs.{extension}")
@bot.command(aliases=["st"])
async def stop(ctx,extension):
	for filename in os.listdir("./cogs"):
		for file in os.listdir("./cogs/"+filename):
			if file.endswith(".py"):
				bot.unload_extension("cogs."+filename+f".{file[:-3]}")
	for filename in os.listdir("./cogs"):
		for file in os.listdir("./cogs/"+filename):
			if file.endswith(".py"):
				bot.load_extension("cogs."+filename+f".{file[:-3]}")
for filename in os.listdir("./cogs"):
	for file in os.listdir("./cogs/"+filename):
		if file.endswith(".py"):
			bot.load_extension("cogs."+filename+f".{file[:-3]}")

async def help(ctx):
	embed=discord.Embed(colour=discord.Color.blue())
	embed.add_field(name="Help Menu",value="\n**My prefix is 's!'**\n\n"+" **s!start <#channel>** : Starts spamming in the required channel or current channel\n\n"+"** s!stop** : Stops the bot")
	await ctx.send(embed=embed)
@bot.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.CommandNotFound):
		
		await ctx.send("```This is not a command\n\nType b!help to see the list of commands```")

bot.run(os.getenv("BOT_TOKEN"))
