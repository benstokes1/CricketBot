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
async def stop(ctx):
	channel=ctx.message.channel
	await channel.edit(topic="stop :1") 
				
for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
			bot.load_extension(f"cogs.{filename[:-3]}")
@bot.command()
async def help(ctx):
	embed=discord.Embed(colour=discord.Color.blue())
	embed.add_field(name="Help Menu",value="\n**My prefix is 'spam'**\n\n"+" **spam start <time>(s,m,h,d) ** : Starts spamming in the required channel or current channel\n\n"+"** spam stop** : Stops the bot\n\n"+" **spam link** : Sends bot link")
	await ctx.send(embed=embed)
@bot.command()
async def invite(ctx):
	await ctx.send("https://discordapp.com/api/oauth2/authorize?client_id=650654612545732618&permissions=8&scope=bot")
@bot.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.CommandNotFound):
		
		await ctx.send("```This is not a command\n\nType s!help to see the list of commands```")

bot.run(os.getenv("BOT_TOKEN"))
