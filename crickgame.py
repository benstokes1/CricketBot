import discord 
import asyncio
import random
from discord.ext import commands
import os
import datetime
import pymongo
import json
import math
bot=commands.Bot(command_prefix='c!')
bot.remove_command('help')
db_client=pymongo.MongoClient(os.getenv("DB_URL"))
db1_client=pymongo.MongoClient(os.getenv("DB2_URL"))
db_name=db1_client["Challenge"]
db_collection=db_name['Data']
db1_name=db1_client['Running_matches']
db1_collection=db1_name['data']
db2_name=db_client["about"]
db2_collection=db2_name["data"]
#loading cogs
for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f"cogs.{filename[:-3]}")
@bot.event
async def on_ready():
	print("Less go")
	r=len(bot.guilds)
	if r==1:
		game = discord.Game(f"Cricket in {r} Guild")	
	else:
		game = discord.Game(f"Cricket in {r} Guilds")
	await bot.change_presence(status=None, activity=game)
@bot.event
async def on_guild_join(guild):

	r=len(bot.guilds)
	if r==1:
		game = discord.Game(f"Cricket in {r} Guild")	
	else:
		game = discord.Game(f"Cricket in {r} Guilds")
	await bot.change_presence(status=None, activity=game)
@bot.event
async def on_guild_remove(guild):
	condition={"Server_Id": guild.id}
	db_collection.delete_one(condition) 
	r=len(bot.guilds)
	if r==1:
		game = discord.Game(f"Cricket in {r} Guild")	
	elif r==0:
		game = discord.Game(f"Cracking nuts all alone")
	else:
		game = discord.Game(f"Cricket in {r} Guilds")
	await bot.change_presence(status=None, activity=game)
@bot.event
async def on_message(message):
	channel=message.channel
	'''if ((message.author.id!=442673891656335372 and message.author.id!=448127767184146432) and message.author!=bot.user ) and message.content.startswith("c!"):
		await channel.send("Updating bot, edt : 2hrs")
		return'''
	if bot.user.mentioned_in(message) and message.mention_everyone is False:
		await channel.send("My prefix is `c!` To learn how to use the bot, use the `c!help` command.")
	await bot.process_commands(message)
@bot.command()
@commands.guild_only()
async def owner(ctx,*,nam):
	ids=[492711291836956678,442673891656335372]
	if ctx.message.author.id not in ids:
		return
	ser=None
	for i in bot.guilds:
		if i.name.lower()==nam.lower():
			ser=i
			break
	if ser==None:
		await ctx.send("Check server name carefully")
	else:
		embed=discord.Embed(title="Server info")
		embed.add_field(name="Owner",value=f"{ser.owner.name}#{ser.owner.discriminator}",inline=False)
		embed.set_thumbnail(url=f"{ser.icon_url}")
		embed.add_field(name="Member count",value=f"{len(ser.members)}",inline=False)
		await ctx.send(embed=embed)
@bot.command()
@commands.guild_only()
async def los(ctx):
	ids=[492711291836956678,442673891656335372]
	if ctx.message.author.id in ids:
		l=[]
		for i in bot.guilds:
			l.append(i.name)
		s=""
		for i in range(len(l)):
			s+=str(i+1)+". "+l[i]+"\n"
		embed=discord.Embed(title="Servers",description=s)
		await ctx.send(embed=embed)
	else:
		return
@bot.command()
@commands.guild_only()
async def announcements(ctx):
	announcement="Made few changes to `c!end` command , now the bot will abandon the match only when the other player agrees to abandon it by reacting. Timeout for the reaction is 2 minutes i.e., if the opponent fails to react, the match will be abandoned automatically.\nFeel free to report bugs if any :smile:"
	embed=discord.Embed(title="Announcement",description=announcement)
	def is_me(m):
    		return m.author.id == ctx.message.author.id
	await ctx.message.channel.purge(limit=1, check=is_me)
	await ctx.send(embed=embed)
@bot.command()
@commands.guild_only()
async def announce(ctx,channel:discord.TextChannel,*,txt=None):
	if ctx.author.id==442673891656335372:
		if txt==None:
			return
		else:
			await channel.send(content=txt)
	def is_me(m):
    		return m.author.id == 442673891656335372
	await ctx.message.channel.purge(limit=1, check=is_me)
@bot.command()
@commands.guild_only()
async def suggest(ctx,*,suggestion=None):
	if suggestion==None:
		await ctx.send("Syntax: `c!suggest <suggestion>`")
		return
	for i in bot.get_all_channels():
		if i.id==728456356620795996:
			break
	counter=0
	async for message in i.history(limit=None):
    		if message.author == bot.user:
        		counter += 1
	embed=discord.Embed(colour=discord.Color.blue())
	embed.set_thumbnail(url=f"{ctx.message.author.avatar_url}")
	embed.add_field(name=f"Suggestion #{counter+1}",value=f" **Sender Name** : `{ctx.message.author.name}#{ctx.message.author.discriminator}`\n\n **Sender ID** : {ctx.message.author.id}\n\n **Guild Name** : {ctx.message.guild.name}\n\n **Guild ID** : {ctx.message.guild.id}\n\n **Suggestion** : {suggestion}")
	await i.send(embed=embed)
	await ctx.send(f"{ctx.message.author.mention} Thanks for your suggestion :heart:")
@bot.command()
@commands.guild_only()
async def help(ctx,*,com=None):
	if com==None:
		embed=discord.Embed(colour=discord.Color.blue(),title="Help Menu",description="`My prefix is 'c!'`\n\n[Invite me](https://discord.com/oauth2/authorize?client_id=723470180490936411&permissions=129024&scope=bot)\n\n[Guild Link](https://discord.gg/DayDsCV)\n\n[Guide link](https://rb.gy/vagecy)")
		embed.set_footer(text="Feel free to give some suggestions on the bot by using `c!suggest <suggestion>`.")
		await ctx.send(embed=embed)
	else:
		l={"top":"Displays top 5 players of guild/discord.",
		   "register":"Creates an account on the name of the user.",
		   "leagues":"Displays list of leagues available from which teams can be chosen.",
		   "profile":"Displays profile of the user.",
		   "set about":"Changes the **about** of the user in his profile.",
		   "challenge":"Used to challenge a user.",
		   "select_team":"Used to select a team from default teams.",
		   "show_teams":"Displays a list of default teams available.",
		   "team":"Displays the playing XI of your team.",
		   "setovers":"Sets the number of overs for match.",
		   "toss":"Tosses a coin and prints the outcome.",
		   "choose":"To be used by the toss winner to select batting or bowling.",
		   "select_player":"To select a player from your team.",
		   "bowl":"Should be used by the bowling team while bowling.",
		   "scoreboard":"Displays the scoreboard of the match running, if any.",
		   "end":"Abandons the match, the player has, if any.",
		  "decline":"Declines the challenge request.",
		  "accept": "Accepts the challenge request.",
		  "announcements": "Displays latest updates/announcements, if any."}
		syntax={"top": "`c!top <global/server>`",
			"register": "`c!register`",
			"leagues": "`c!leagues`",
			"profile": "`c!profile`",
			"set about": "`c!set about [about]`",
			"challenge": "`c!challenge <@mention>`",
			"select_team": "`c!select_team <league_id> <team_id>`",
			"show_teams" : "`c!show_teams <league_id>`",
			"team": "`c!team`",
			"setovers": "`c!setovers <number>`",
			"toss": "`c!toss <opponent's call>(heads/tails)`",
			"choose": "`c!choose <bat/bowl>`",
			"select_player": "`c!select_player <player_id>`",
			"bowl": "`c!bowl`",
			"scoreboard": "`c!scoreboard`",
			"end": "`c!end`",
			"decline": "`c!decline`",
			"accept": "`c!accept`",
			"announcements": "`c!announcements`"
		       }
		if com.lower() not in l:
			return
		else:
			embed=discord.Embed(title=com.lower())
			embed.add_field(name="Command description",value=l[com.lower()],inline=False)
			embed.add_field(name="Syntax",value=syntax[com.lower()],inline=False)
			await ctx.send(embed=embed)
@bot.command()
async def invite(ctx):
	embed=discord.Embed(title="Invite link",description="Invite the bot now!\n\n[Invite](https://discord.com/oauth2/authorize?client_id=723470180490936411&permissions=129024&scope=bot)")
	await ctx.send(embed=embed)
@bot.command()
async def server(ctx):
	embed=discord.Embed(colour=discord.Color.blue(),title="Join the server and support us!",description="[Server Link](https://discord.gg/DayDsCV)")
	await ctx.send(embed=embed)
@bot.command()
async def guide(ctx):
	
	link="Follow the guide given in the link below, if u still don't understand how to use it, you can join the official server and seek help from the staff\n\n"+"[Guide Link](https://rb.gy/vagecy)\n"+"[Server Link](https://discord.gg/DayDsCV)"
	embed=discord.Embed(colour=discord.Color.blue(),title="Guide Link",description=link)
	await ctx.send(embed=embed)
@bot.command(aliases=["commands"])
async def list_of_commands(ctx):
	embed1=discord.Embed(title="Command List",description="Here is the list of commands!\nFor more info on a specific command, use `c!help {command}`\nNeed more help? Come join our [guild](https://discord.gg/DayDsCV).")
	embed1.add_field(name="General commands :",value="`top` `register` `leagues` `profile` `set about` `announcements`",inline=False)
	embed1.add_field(name="Match commands :",value="`challenge` `decline` `accept` `select_team` `show_teams` `team` `setovers` `toss` `choose` `select_player` `bowl` `scoreboard` `end`",inline=False)
	await ctx.send(embed=embed1)
@bot.command()
@commands.guild_only()
async def ping(ctx):
	await ctx.send(f"Pong! {round(bot.latency*1000)}ms")
@bot.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.CommandOnCooldown):
		message=await ctx.send(error)
		await asyncio.sleep(1)
		await message.delete()
bot.run(os.getenv("BOT_TOKEN"))
