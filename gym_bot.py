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
	embed=discord.Embed(colour=discord.Color.blue())
	embed.add_field(name="Help Menu",value="\n**My prefix is 'b!'**\n\n"+"__`Trainer Commands:`__\n\n"+" **b!gym_details <name of gym> (example b!gd fire)** :  Gives gym details\n\n **b!gym_leaders** : Gives the list of gym leaders\n\n **b!trainer_card** : Shows the badges owned by the trainer\n\n"+"__`Gym Leader Commands:`__\n\n"+" **b!start_duel <@mention>(trainer)** : To be used before u start a gym battle\n\n **b!give_badge <@mention>** : Gives the mentioned user badge\n\n **b!clear <number>** : Clears the messages\n\n **b!leader_card <name of gym>** : Displays the gym leader card\n\n **b!store** : Displays the Gym leader store")
	await ctx.send(embed=embed)
@bot.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.CommandNotFound):
		
		await ctx.send("```This is not a command\n\nType b!help to see the list of commands```")

bot.run(os.getenv("BOT_TOKEN"))
