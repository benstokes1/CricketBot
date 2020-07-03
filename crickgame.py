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
	if bot.user.mentioned_in(message) and message.mention_everyone is False:
		await channel.send("My prefix is `c!` To learn how to use the bot, use the `c!help` command.")
	await bot.process_commands(message)

@bot.command()
async def announce(ctx,*,txt=None):
	channel=bot.get_channel(728507676379840532)
	if ctx.author.id==442673891656335372:
		if txt==None:
			pass
		else:
			await channel.send(txt)
@bot.command()
async def guide(ctx):
	
	link="Follow the guide given in the link below, if u still don't understand how to use it, you can join the official server and seek help from the staff\n\n"+"[Guide Link](https://rb.gy/vagecy)\n"+"[Server Link](https://discord.gg/DayDsCV)"
	embed=discord.Embed(colour=discord.Color.blue(),title="Guide Link",description=link)
	await ctx.send(embed=embed)
@bot.command()
async def ping(ctx):
	await ctx.send(f"Pong! {round(bot.latency*1000)}ms")
@bot.command()
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
async def help(ctx):
	embed=discord.Embed(colour=discord.Color.blue(),title="Help Menu",description="My prefix is 'c!'")
	embed.add_field(name="c!commands",value="Displays a list of commands",inline=False)
	embed.add_field(name="c!invite",value="Sends an Invite Link of the bot",inline=False)
	embed.add_field(name="c!server",value="Sends an invite link of official discord server of the bot",inline=False)
	embed.add_field(name="c!guide",value="Sends a link of the guide",inline=False)
	embed.set_footer(text="Feel free to give some suggestions on the bot by using `c!suggest <suggestion>`.")
	await ctx.send(embed=embed)
@bot.command()
async def invite(ctx):
	embed=discord.Embed(title="Invite link",description="Invite the bot now!\n\n[Invite](https://discord.com/oauth2/authorize?client_id=723470180490936411&permissions=129024&scope=bot)")
	await ctx.send(embed=embed)
@bot.command()
async def server(ctx):
	embed=discord.Embed(colour=discord.Color.blue(),title="Join the server and support us!",description="[Server Link](https://discord.gg/DayDsCV)")
	await ctx.send(embed=embed)
@bot.command(aliases=["commands"])
async def list_of_commands(ctx):
	embed=discord.Embed(title="List of commands",description="My prefix is 'c!'\n\n`General commands :`")
	embed.add_field(name="c!register",value="Creates an account on the name of the user which will be useful",inline=False)
	embed.add_field(name="c!profile",value="Displays profile of the user",inline=False)
	embed.add_field(name="c!set about",value="Sets the about of the user in his profile\n\n`Match commands :`",inline=False)
	embed.add_field(name="c!challenge <@mention>",value="Used to challenge a user",inline=False)
	embed.add_field(name="c!select_team",value="Used to select a team from default teams.",inline=False)
	embed.add_field(name="c!show_teams",value="Displays a list of default teams available.",inline=False)
	embed.add_field(name="c!team",value="Displays the playing XI of your team.",inline=False)
	embed.add_field(name="c!setovers <number>",value="Sets the number of overs for match.",inline=False)
	embed.add_field(name="c!toss <opponent's call>",value="Tosses a coin and prints the outcome.",inline=False)
	embed.add_field(name="c!choose <bat/bowl>",value="To be used by the toss winner to select batting or bowling.",inline=False)
	embed.add_field(name="c!select_player",value="To select a player from your team.",inline=False)
	embed.add_field(name="c!bowl",value="Should be used by the bowling team while bowling.",inline=False)
	embed.add_field(name="c!scoreboard",value="Displays the scoreboard of the match running, if any.",inline=False)
	embed.add_field(name="c!end",value="Abandons the match the player has if any.",inline=False)
	await ctx.send(embed=embed)
@bot.command()
async def challenge(ctx,Team2:discord.Member=None):
	if Team2==None:
		await ctx.send("Syntax `c!challenge <@mention>`")
		return
	Team1_id=ctx.message.author.id
	Team2_id=Team2.id
	if Team2.bot==True:
		await ctx.send("Tag a human not a bot")
		return
	if Team2.id==Team1_id:
		await ctx.send("Dont tag urself")
		return
	h=db2_collection.find_one({"id":Team2.id})
	h1=db2_collection.find_one({"id":ctx.message.author.id})
	if h1==None or h==None:
		if h1==None:
			await ctx.send("You need to have an account to challenge a person\nType `c!register` to create an account")
			return
		else:
			await ctx.send(f"{Team2.mention} doesn't have an account\nType `c!register` to create an account")
			return
	x=db1_collection.find_one()
	if x==None:
		pass
	elif ctx.message.author.id in x["ids"] or Team2_id in x["ids"]:
		h=db2_collection.find_one({"id":ctx.message.author.id})
		original_name=ctx.author.name
		if h==None:
			original_name=Team2.name
			h=db2_collection.find_one({"id":Team2_id})
		await ctx.send(f"**{original_name}** finish your undone match with **{h['now_match']}** or type `c!end` to end the match")
		return
	x["ids"].append(Team2_id)
	x['ids'].append(Team1_id)
	opponent_1=ctx.message.author.name+"#"+str(ctx.message.author.discriminator)
	db2_collection.update_one({"id": Team2_id},{"$set":{"now_match": opponent_1}})
	opponent_1=Team2.name+"#"+Team2.discriminator
	db2_collection.update_one({"id":Team1_id},{"$set":{"now_match": opponent_1}})
	outline={
    "Team1_name": "None",
    "Team2_name": "None",
    "Team1_member_id": Team1_id,
    "Team2_member_id": Team2_id,
	"Maximum_overs":0,
	"Now_batting": 0,
    "Team1_data":{
        "Lineup":[],
        "Batting": {},
        "Bowling": {},
		"Current_batting": [],
		"Current_bowling": [],
		"Previous_bowler": [],
        "Batsmen_out": []
    },
    "Team2_data":{
        "Lineup":[],
        "Batting": {},
        "Bowling": {},
		"Current_batting": [],
		"Current_bowling": [],
		"Previous_bowler": [],
        "Batsmen_out": []
    },
	"Score_card": {
			"Target": 0,
			"Overs": "0.0",
			"Maximum_overs": "0.0",
			"Last_ball": "0",
			"Score": 0,
			"Wickets": 0,
			"Toss": 0,
			"First_innings_score": "0" 
		} ,
    "First_innings_score": "",
    "This_over": "",
	"Maximum_wickets": 10
	}
	db1_collection.update_one({},{"$set":{"ids":x['ids']}})
	db_collection.insert_one(outline)
	await ctx.send("Select Teams by typing `c!select_team`")
@bot.command(aliases=["pe"])
async def team(ctx,number=None):
	with open ("./Teams/IPL.json") as f:
		d=json.load(f)
	
	x=db_collection.find_one({"Team1_member_id":ctx.message.author.id})
	if x==None:
		x=db_collection.find_one({"Team2_member_id":ctx.message.author.id})
		if x==None:
			return
		if x["Team2_name"]=="None":
			return
		player_list=""
		for i in range(len(d[x["Team2_name"]])):
			player_list+=str(i+1)+". "+d[x['Team2_name']][i]+"\n"
		embed=discord.Embed(title=f"{x['Team2_name']} Playin XI",description=player_list)
		await ctx.send(embed=embed)
	else:
		if x["Team1_name"]=="None":
			return
		player_list=""
		for i in range(len(d[x["Team1_name"]])):
			player_list+=str(i+1)+". "+d[x['Team1_name']][i]+"\n"
		embed=discord.Embed(title=f"{x['Team1_name']} Playin XI",description=player_list)
		await ctx.send(embed=embed)
@bot.command(aliases=["ct","st","show_teams"])
async def select_team(ctx,number=None):
	with open ("./Teams/IPL.json") as f:
		d=json.load(f)
	available_teams=[]
	for i in d:
		available_teams.append(i)
	team_list=""
	for i in range(len(available_teams)):
		team_list+=str(i+1)+". "+available_teams[i]+"\n"
	if number==None:
		embed=discord.Embed(title="Teams",description=team_list)
		embed.set_footer(text="To select a team use `c!select_team <number>`")
		await ctx.send(embed=embed)
	else:
		try:
			number=int(number)-1
		except:
			return
		x=db_collection.find_one({"Team1_member_id": ctx.message.author.id})
		if x==None:
			x=db_collection.find_one({"Team2_member_id": ctx.message.author.id})
			if x==None:
				return
			else:
				player_list=""
				for i in range(len(d[available_teams[number]])):
					player_list+=str(i+1)+". "+d[available_teams[number]][i]+"\n"
				if x["Team2_name"]!="None":
					await ctx.send("Can't change your team once after u chose it")
					return
				if x["Team1_name"]!="None" and x["Team1_name"]==available_teams[number]:
					await ctx.send(f"The other player already chose {available_teams[number]}\nChoose an other team")
					return
				x["Team2_name"]=available_teams[number]
				db_collection.update_one({"Team2_member_id": ctx.message.author.id},{"$set":{"Team2_name":available_teams[number],"Team2_data.Lineup":d[available_teams[number]]}})
				embed=discord.Embed(title="Teams",description=player_list)
				await ctx.send(content=f"**{available_teams[number]}** selected\n`Heres the list of playin XI`",embed=embed)
				if x["Team2_name"]!="None" and x["Team1_name"]!="None":
					await ctx.send("Set the overs by typing `c!set_overs`")
					return
		else:
			if x["Team1_name"]!="None":
				await ctx.send("Can't change your team once after u chose it")
				return
			if x["Team2_name"]!="None" and x["Team2_name"]==available_teams[number]:
					await ctx.send(f"The other player already chose {available_teams[number]}\nChoose an other team")
					return
			x["Team1_name"]=available_teams[number]
			player_list=""
			for i in range(len(d[available_teams[number]])):
				player_list+=str(i+1)+". "+d[available_teams[number]][i]+"\n"
			db_collection.update_one({"Team1_member_id": ctx.message.author.id},{"$set":{"Team1_name":available_teams[number],"Team1_data.Lineup":d[available_teams[number]]}})
			embed=discord.Embed(title="Teams",description=player_list)
			await ctx.send(content=f"**{available_teams[number]}** selected\n`Here's the list of playing XI`",embed=embed)
			if x["Team2_name"]!="None" and x["Team1_name"]!="None":
				await ctx.send("Set the overs by typing `c!set_overs`")
				return
@bot.command(aliases=["so"])
async def setovers(ctx,number=None):
	if number==None:
		await ctx.send("Syntax: `c!set_overs <number>`")
	x=db_collection.find_one({"Team1_member_id":ctx.message.author.id})
	if x==None:
		x=db_collection.find_one({"Team2_member_id":ctx.message.author.id})
		if x==None:
			return
		else:
			if x["Maximum_overs"]!=0:
				await ctx.send("Can't change the overs once set")
				return
			if x["Team2_name"] =="None" or x["Team1_name"] =="None":
				await ctx.send("Overs can be set only after choosing teams")
				return
			try:
				number=int(number)		
				db_collection.update_one({"Team2_member_id": ctx.message.author.id},{"$set":{"Maximum_overs":number,"Score_card.Maximum_overs": str(number)+".0"}})
				await ctx.channel.send("Overs set successfully\nNow go for the toss. Syntax: `c!toss <opponent's call>`")
			except:
				await ctx.send("Syntax: `c!set_overs <number>`")
				return
	else:
		if x["Maximum_overs"]!=0:
			await ctx.send("Can't change the overs once set")
			return
	
		if x["Team2_name"]=="None" or x["Team1_name"]=="None":
			await ctx.send("Overs can be set only after choosing teams")
			return	
		try:
			number=int(number)		
			db_collection.update_one({"Team1_member_id": ctx.message.author.id},{"$set":{"Maximum_overs": number,"Score_card.Maximum_overs": str(number)+".0"}})
			await ctx.channel.send("Overs set successfully\nNow go for the toss. Syntax: `c!toss <opponent's call>`")
		except:

			await ctx.send("Syntax: `c!set_overs <number>`")
			return
@bot.command(aliases=["t"])
async def toss(ctx,choice=None):
	#toss
	if choice==None:
		pass
	elif choice.title() not in ["Heads","Tails"]:
		await ctx.send("Syntax: `c!toss <opponent's call>`")
		return
	
	outcomes=["Heads","Tails"]
	answer=random.choice(outcomes)
	embed=discord.Embed(title='Toss')
	embed.set_image(url="https://i.pinimg.com/originals/d7/49/06/d74906d39a1964e7d07555e7601b06ad.gif")
	message=await ctx.send(embed=embed)
	await asyncio.sleep(5)	
	embed=discord.Embed(title=f'Oh! Its a {answer}')
	await message.edit(embed=embed)
	x=db_collection.find_one({"Team1_member_id": ctx.message.author.id})
	if x==None:
		x=db_collection.find_one({"Team2_member_id": ctx.message.author.id})
		if x==None:
			return
		else:
			if x["Maximum_overs"]==0:
				await ctx.send("Toss can be done only after setting overs")
				return
			if x["Score_card"]["Toss"]!=0:
				return
			if choice==None:
				return
			if x["Team1_member_id"]==ctx.message.author.id:
				caller=x["Team2_name"]
				tosser=x["Team1_name"]
			else:
				tosser=x["Team2_name"]
				caller=x["Team1_name"]
			if choice.title()==answer:
				x=db_collection.update_one({"Team2_member_id": ctx.message.author.id},{"$set":{"Score_card.Toss": x["Team1_member_id"]}})	
				await ctx.send(f"**{caller}** won the toss\n**Note:** Use `c!choose <bat/bowl>` to choose batting or bowling")
			else:
				x=db_collection.update_one({"Team2_member_id": ctx.message.author.id},{"$set":{"Score_card.Toss": x["Team2_member_id"]}})	
				await ctx.send(f"**{tosser}** won the toss\n**Note:** Use `c!choose <bat/bowl>` to choose batting or bowling")
	else:
	
		if x["Maximum_overs"]==0:
			await ctx.send("Toss can be done only after setting overs")
			return
		if x["Score_card"]["Toss"]!=0:
			return
		if choice==None:
			return
		if x["Team1_member_id"]==ctx.message.author.id:
			caller=x["Team2_name"]
			tosser=x["Team1_name"]
		else:
			tosser=x["Team2_name"]
			caller=x["Team1_name"]
		if choice.title()==answer:
			x=db_collection.update_one({"Team1_member_id": ctx.message.author.id},{"$set":{"Score_card.Toss": x["Team2_member_id"]}})	
			await ctx.send(f"**{caller}** won the toss\n**Note:** Use `c!choose <bat/bowl>` to choose batting or bowling")
		else:
			x=db_collection.update_one({"Team1_member_id": ctx.message.author.id},{"$set":{"Score_card.Toss": x["Team1_member_id"]}})	
			await ctx.send(f"**{tosser}** won the toss\n**Note:** Use `c!choose <bat/bowl>` to choose batting or bowling")
@bot.command(aliases=["c"])
async def choose(ctx,choice=None):
	if choice==None:
		return
	if choice.lower() not in ["bowl","bat"]:
		await ctx.send("Syntax: `c!choose <bowl/bat>`")
		return
	x=db_collection.find_one({"Team1_member_id": ctx.message.author.id})
	if x==None:
		x=db_collection.find_one({"Team2_member_id": ctx.message.author.id})
		if x==None:
			await ctx.send("Type `c!help` to know about how to use the bot!")
			return
		else:
			if x["Now_batting"]!=0:
				return
			if x["Score_card"]["Toss"]==0:
				await ctx.send("Make sure you do the toss before choosing")
				return

			if x["Score_card"]["Toss"]!=ctx.message.author.id:
				await ctx.send("Looks like you didn't win the toss")
				return
			else:
				if choice.lower()=="bat":
					db_collection.update_one({"Team2_member_id": ctx.message.author.id},{"$set":{"Now_batting": ctx.message.author.id}})
					if x["Team2_name"]=="None":
						await ctx.send("Team 2 will be batting first")
					else:
						await ctx.send(f"**{x['Team2_name']}** will be batting first")
				else:
					db_collection.update_one({"Team2_member_id": ctx.message.author.id},{"$set":{"Now_batting": x["Team1_member_id"]}})
					if x["Team1_name"]=="None":
						await ctx.send("Team 1 will be batting first")
					else:
						await ctx.send(f"**{x['Team1_name']}** will be batting first")
	else:
		if x["Now_batting"]!=0:
			return
		if x["Score_card"]["Toss"]==0:
			await ctx.send("Make sure you do the toss before choosing")
			return
		if x["Score_card"]["Toss"]!=ctx.message.author.id:
			await ctx.send("Looks like you didn't win the toss")
			return
		else:
			if choice.lower()=="bat":
				db_collection.update_one({"Team1_member_id": ctx.message.author.id},{"$set":{"Now_batting": ctx.message.author.id}})
				if x["Team1_name"]=="None":
					await ctx.send("Team 1 will be batting first")
				else:
					await ctx.send(f"**{x['Team1_name']}** will be batting first")
			else:
				db_collection.update_one({"Team1_member_id": ctx.message.author.id},{"$set":{"Now_batting": x["Team2_member_id"]}})
				if x["Team2_name"]=="None":
					await ctx.send("Team 2 will be batting first")
				else:
					await ctx.send(f"**{x['Team2_name']}** will be batting first")
@bot.command(aliases=["sp"])
async def select_player(ctx,number=None,number1=None):
	x=db_collection.find_one({"Team1_member_id": ctx.message.author.id})
	if x==None:
		x=db_collection.find_one({"Team2_member_id": ctx.message.author.id})
		if x==None:
			await ctx.send("Type `c!help` to know about how to use the bot!")
			return
		else:
			if x["Now_batting"]==0:
				await ctx.send("Type `c!help` to know about how to use the bot!")
				return
			if x["Team2_name"]=="None":
				await ctx.send("Looks like you didn't choose a team!\nType `c!select_team` to choose a team")

			else:
				if number==None:
					if x["Now_batting"]==x["Team2_member_id"]:
						team_list=""
						for i in range(len(x["Team2_data"]["Lineup"])):
							if x["Team2_data"]["Lineup"][i] in x["Team2_data"]["Batsmen_out"]:
								team_list+=str(i+1)+". ~~"+x["Team2_data"]["Lineup"][i]+"~~(out)\n"
							elif x["Team2_data"]["Lineup"][i] in x["Team2_data"]["Current_batting"]:
								team_list+=str(i+1)+". **"+x["Team2_data"]["Lineup"][i]+"**\n"
							else:
								team_list+=str(i+1)+". "+x["Team2_data"]["Lineup"][i]+"\n"
							embed=discord.Embed(title=f"{x['Team2_name']}",description=f"{team_list}")
							if len(x["Team2_data"]["Current_batting"])==0:
								embed.set_footer(text="Type `c!select_player <number1> <number2>` to choose opening batsmen")
							else:
								embed.set_footer(text="Type `c!select_player <number>` to choose batsmen")
							
					else:
						team_list=""
						max_balls=int(math.ceil(x["Maximum_overs"]/5))*6
						for i in range(len(x["Team2_data"]["Lineup"])):
							if x["Team2_data"]["Lineup"][i] in x["Team2_data"]["Previous_bowler"]:
								team_list+=str(i+1)+". ~~"+x["Team2_data"]["Lineup"][i]+"~~(last over)\n"
								continue
							if x["Team2_data"]["Lineup"][i] in x["Team2_data"]["Current_bowling"]:
								team_list+=str(i+1)+". **"+x["Team2_data"]["Lineup"][i]+"**\n"
								continue
							else:							
								if len(list(x["Team2_data"]["Bowling"].keys()))==0:
									pass
								else:
									if x["Team2_data"]["Lineup"][i] in x["Team2_data"]["Bowling"]:
										if x["Team2_data"]["Bowling"][x["Team2_data"]["Lineup"][i]]["balls_thrown"]==max_balls:
											team_list+=str(i+1)+". ~~"+x["Team2_data"]["Lineup"][i]+"~~(quota over)\n"
										else:
											pass
									else:
										pass
							team_list+=str(i+1)+". "+x["Team2_data"]["Lineup"][i]+"\n"
						embed=discord.Embed(title=f"{x['Team2_name']}",description=f"{team_list}")
						embed.set_footer(text="Type `c!select_player <number>` to choose bowler")
					await ctx.send(embed=embed)
				else:
					try:
						number=int(number)-1
						if number1==None:
							pass
						else:
							number1=int(number1)-1
					except:
						return
					if x["Now_batting"]==x["Team2_member_id"]:
						if number>10:
							await ctx.send("Choose a number less than 11")
							return
						if number1!=None:
							if number1>10:
								await ctx.send("Choose a number less than 11")
								return
						if len(x["Team2_data"]["Current_batting"])==0:
							if number1==None:
								await ctx.send("Syntax: `c!select_player <number1> <number2>`")
								return
							data={x["Team2_data"]["Lineup"][number]:{
								"runs":0,
								"balls_faced":0},x["Team2_data"]["Lineup"][number1]:{
								"runs":0,
								"balls_faced":0}}
							for i in data:
								x["Team2_data"]["Batting"][i]=data[i]
							db_collection.update_one({"Team2_member_id": ctx.message.author.id},{"$set":{"Team2_data.Current_batting":[x["Team2_data"]["Lineup"][number],x["Team2_data"]["Lineup"][number1]],"Team2_data.Batting": x["Team2_data"]["Batting"]}})
							await ctx.send(f"{x['Team2_data']['Lineup'][number]} and {x['Team2_data']['Lineup'][number1]} have been sent to the crease")
						elif len(x["Team2_data"]["Current_batting"])==1:
							if x["Team2_data"]["Lineup"][number] in x["Team2_data"]["Current_batting"]:
								await ctx.send("He is already on the ground")
								return
							elif x["Team2_data"]["Lineup"][number] in x["Team2_data"]["Batsmen_out"]:
								await ctx.send("He got out already")
								return
							else:
								data={x["Team2_data"]["Lineup"][number]:{
								"runs":0,
								"balls_faced":0
								}}
								for i in data:
									x["Team2_data"]["Batting"][i]=data[i]
								x["Team2_data"]["Current_batting"].insert(0,x["Team2_data"]["Lineup"][number])
								db_collection.update_one({"Team2_member_id": ctx.message.author.id},{"$set":{"Team2_data.Current_batting": x["Team2_data"]["Current_batting"],"Team2_data.Batting": x["Team2_data"]["Batting"]}})
								await ctx.send(f"{x['Team2_data']['Lineup'][number]} has been sent to the crease")
						else:
							await ctx.send("No wicket has fallen yet")
							return
					else:
						if len(x["Team2_data"]["Current_bowling"])==1:
							await ctx.send("Over hasnt completed yet")
							return
						else:
							if number>10:
								await ctx.send("Choose a number less than 11")
								return
							if x["Team2_data"]["Lineup"][number] in x["Team2_data"]["Bowling"]:
								max_balls=int(math.ceil(x["Maximum_overs"]/5))*6
								if x["Team2_data"]["Bowling"][x["Team2_data"]["Lineup"][number]]["balls_thrown"]==max_balls:
									await ctx.send("This bowler has already completed his quota")
								elif x["Team2_data"]["Lineup"][number] in x["Team2_data"]["Previous_bowler"]:
									await ctx.send("A bowler cannot bowl 2 consecutive overs, choose someone else")
								else:
									db_collection.update_one({"Team2_member_id": ctx.message.author.id},{"$set":{"Team2_data.Current_bowling": [x["Team2_data"]["Lineup"][number]]}})
									number_of_overs=x["Score_card"]["Overs"].split(".")
									number_of_overs=int(number_of_overs[0])+1
									if number_of_overs==1:
										await ctx.send(f"{x['Team2_data']['Lineup'][number]} will bowl the {number_of_overs}st over")
									elif number_of_overs==2:
										await ctx.send(f"{x['Team2_data']['Lineup'][number]} will bowl the {number_of_overs}nd over")
									elif number_of_overs==3:
										await ctx.send(f"{x['Team2_data']['Lineup'][number]} will bowl the {number_of_overs}rd over")
									else:
										await ctx.send(f"{x['Team2_data']['Lineup'][number]} will bowl the {number_of_overs}th over")
									
							else:
								data={x["Team2_data"]["Lineup"][number]:{
										"runs": 0,
										"balls_thrown": 0,
										"wickets": 0
									}}
								for i in data:
									x["Team2_data"]["Bowling"][i]=data[i]
								db_collection.update_one({"Team2_member_id": ctx.message.author.id},{"$set":{"Team2_data.Current_bowling": [x["Team2_data"]["Lineup"][number]],"Team2_data.Bowling": x["Team2_data"]["Bowling"]}})
								number_of_overs=x["Score_card"]["Overs"].split(".")
								number_of_overs=int(number_of_overs[0])+1
								if number_of_overs==1:
									await ctx.send(f"{x['Team2_data']['Lineup'][number]} will bowl the {number_of_overs}st over")
								elif number_of_overs==2:
									await ctx.send(f"{x['Team2_data']['Lineup'][number]} will bowl the {number_of_overs}nd over")
								elif number_of_overs==3:
									await ctx.send(f"{x['Team2_data']['Lineup'][number]} will bowl the {number_of_overs}rd over")
								else:
									await ctx.send(f"{x['Team2_data']['Lineup'][number]} will bowl the {number_of_overs}th over")
	else:
	
		if x["Now_batting"]==0:
			await ctx.send("Type `c!help` to know about how to use the bot!")
			return
		if x["Team1_name"]=="None":
			await ctx.send("Looks like you didn't choose a team!\nType `c!select_team` to choose a team")
		else:
			if number==None and number1==None:
				if x["Now_batting"]==x["Team1_member_id"]:
					team_list=""
					for i in range(len(x["Team1_data"]["Lineup"])):
						if x["Team1_data"]["Lineup"][i] in x["Team1_data"]["Batsmen_out"]:
							team_list+=str(i+1)+". ~~"+x["Team1_data"]["Lineup"][i]+"~~(out)\n"
						elif x["Team1_data"]["Lineup"][i] in x["Team1_data"]["Current_batting"]:
							team_list+=str(i+1)+". **"+x["Team1_data"]["Lineup"][i]+"**\n"
						else:
							team_list+=str(i+1)+". "+x["Team1_data"]["Lineup"][i]+"\n"
					
					embed=discord.Embed(title=f"{x['Team1_name']}",description=f"{team_list}")
					if len(x["Team1_data"]["Current_batting"])==0:
						embed.set_footer(text="Type `c!select_player <number1> <number2>` to choose opening batsmen")
					else:
						embed.set_footer(text="Type `c!select_player <number>` to choose batsmen")
				else:
					team_list=""
					max_balls=int(math.ceil(x["Maximum_overs"]/5))*6
					for i in range(len(x["Team1_data"]["Lineup"])):
						if x["Team1_data"]["Lineup"][i] in x["Team1_data"]["Previous_bowler"]:
							team_list+=str(i+1)+". ~~"+x["Team1_data"]["Lineup"][i]+"~~(last over)\n"
							continue
						if x["Team1_data"]["Lineup"][i] in x["Team1_data"]["Current_bowling"]:
							team_list+=str(i+1)+". **"+x["Team1_data"]["Lineup"][i]+"**\n"
							continue
						else:
							if len(list(x["Team1_data"]["Bowling"].keys()))==0:
								pass
							else:
								if x["Team1_data"]["Lineup"][i] in x["Team1_data"]["Bowling"]:
									if x["Team1_data"]["Bowling"][x["Team1_data"]["Lineup"][i]]["balls_thrown"]==max_balls:
										team_list+=str(i+1)+". ~~"+x["Team1_data"]["Lineup"][i]+"~~(quota over)\n"
									else:
										pass
								else:
									pass
						team_list+=str(i+1)+". "+x["Team1_data"]["Lineup"][i]+"\n"
					embed=discord.Embed(title=f"{x['Team1_name']}",description=f"{team_list}")
					embed.set_footer(text="Type `c!select_player <number>` to choose bowler")
				

				await ctx.send(embed=embed)
			else:
				try:
					number=int(number)-1
					if number1==None:
						pass
					else:
						number1=int(number1)-1
				except:
					return
				if x["Now_batting"]==x["Team1_member_id"]:
					if number>10:
						await ctx.send("Choose a number less than 11")
						return
					if number1!=None:
						if number1>10:
							await ctx.send("Choose a number less than 11")
							return
					if len(x["Team1_data"]["Current_batting"])==0:
						if number1==None:
							await ctx.send("Syntax: `c!select_player <number1> <number2>`")
							return
						data={x["Team1_data"]["Lineup"][number]:{
							"runs":0,
							"balls_faced":0
						},x["Team1_data"]["Lineup"][number1]:
						{
							"runs":0,
							"balls_faced":0
						}}
						for i in data:
							x["Team1_data"]["Batting"][i]=data[i]
						db_collection.update_one({"Team1_member_id": ctx.message.author.id},{"$set":{"Team1_data.Current_batting":[x["Team1_data"]["Lineup"][number],x["Team1_data"]["Lineup"][number1]],"Team1_data.Batting": x["Team1_data"]["Batting"]}})
						await ctx.send(f"{x['Team1_data']['Lineup'][number]} and {x['Team1_data']['Lineup'][number1]} have been sent to the crease")
					elif len(x["Team1_data"]["Current_batting"])==1:
						if x["Team1_data"]["Lineup"][number] in x["Team1_data"]["Current_batting"]:
							await ctx.send("He is already on the ground")
							return
						elif x["Team1_data"]["Lineup"][number] in x["Team1_data"]["Batsmen_out"]:
							await ctx.send("He got out already")
							return
						else:
							data={x["Team1_data"]["Lineup"][number]:{
							"runs":0,
							"balls_faced":0
							}}
							for i in data:
								x["Team1_data"]["Batting"][i]=data[i]
							x["Team1_data"]["Current_batting"].insert(0,x["Team1_data"]["Lineup"][number])
							db_collection.update_one({"Team1_member_id": ctx.message.author.id},{"$set":{"Team1_data.Current_batting": x["Team1_data"]["Current_batting"],"Team1_data.Batting": x["Team1_data"]["Batting"]}})
							await ctx.send(f"{x['Team1_data']['Lineup'][number]} has been sent to the crease")
					else:
						await ctx.send("No wicket has fallen yet")
						return
				else:

					if len(x["Team1_data"]["Current_bowling"])==1:
						await ctx.send("Over hasnt completed yet")
						return
					else:
						if number>10:
							await ctx.send("Choose a number less than 11")
							return
						if x["Team1_data"]["Lineup"][number] in x["Team1_data"]["Bowling"]:
							max_balls=int(math.ceil(x["Maximum_overs"]/5))*6
							if x["Team1_data"]["Bowling"][x["Team1_data"]["Lineup"][number]]["balls_thrown"]==max_balls:
								await ctx.send("This bowler has already completed his quota")
							elif x["Team1_data"]["Lineup"][number] in x["Team1_data"]["Previous_bowler"]:
								await ctx.send("A bowler cannot bowl 2 consecutive overs, choose someone else")
							else:
								db_collection.update_one({"Team1_member_id": ctx.message.author.id},{"$set":{"Team1_data.Current_bowling": [x["Team1_data"]["Lineup"][number]]}})
								number_of_overs=x["Score_card"]["Overs"].split(".")
								number_of_overs=int(number_of_overs[0])+1
								if number_of_overs==1:
									await ctx.send(f"{x['Team1_data']['Lineup'][number]} will bowl the {number_of_overs}st over")	
								elif number_of_overs==2:
									await ctx.send(f"{x['Team1_data']['Lineup'][number]} will bowl the {number_of_overs}nd over")
								elif number_of_overs==3:
									await ctx.send(f"{x['Team1_data']['Lineup'][number]} will bowl the {number_of_overs}rd over")
								else:
									await ctx.send(f"{x['Team1_data']['Lineup'][number]} will bowl the {number_of_overs}th over")
						else:
							data={x["Team1_data"]["Lineup"][number]:{
									"runs": 0,
									"balls_thrown": 0,
									"wickets": 0
								}}
							for i in data:
								x["Team1_data"]["Bowling"][i]=data[i]
							db_collection.update_one({"Team1_member_id": ctx.message.author.id},{"$set":{"Team1_data.Current_bowling": [x["Team1_data"]["Lineup"][number]],"Team1_data.Bowling": x["Team1_data"]["Bowling"]}})
							number_of_overs=x["Score_card"]["Overs"].split(".")
							number_of_overs=int(number_of_overs[0])+1
							if number_of_overs==1:
								await ctx.send(f"{x['Team1_data']['Lineup'][number]} will bowl the {number_of_overs}st over")
							elif number_of_overs==2:
								await ctx.send(f"{x['Team1_data']['Lineup'][number]} will bowl the {number_of_overs}nd over")
							elif number_of_overs==3:
								await ctx.send(f"{x['Team1_data']['Lineup'][number]} will bowl the {number_of_overs}rd over")
							else:
								await ctx.send(f"{x['Team1_data']['Lineup'][number]} will bowl the {number_of_overs}th over")
@bot.command(aliases=["b"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def bowl(ctx):
	z=None
	txt,img=None,None
	x=db_collection.find_one({"Team1_member_id": ctx.message.author.id})
	if x==None:
		x=db_collection.find_one({"Team2_member_id": ctx.message.author.id})
		if x==None:
			await ctx.send("Type `c!help` to know about how to use the bot!")
			return
		
	This_over=x["This_over"]
	original_data=x
	Batting_team=0
	Bowling_team=0
	if x["Now_batting"]==0:
		return
	if x["Team1_member_id"]==x["Now_batting"]:
		Batting_team_name=x["Team1_name"]
		Bowling_team_name=x["Team2_name"]
		Batting_team_id=x["Team1_member_id"]
		Bowling_team_id=x["Team2_member_id"]
		Batting_team=x["Team1_data"]
		Bowling_team=x["Team2_data"]
	else:
		Batting_team_name=x["Team2_name"]
		Bowling_team_name=x["Team1_name"]
		Batting_team_id=x["Team2_member_id"]
		Bowling_team_id=x["Team1_member_id"]
		Batting_team=x["Team2_data"]
		Bowling_team=x["Team1_data"]
	if len(Batting_team["Current_batting"])<=1 or len(Bowling_team["Current_bowling"])==0:
		if len(Batting_team["Current_batting"])<=1:
			await ctx.send("Choose the batsman using `c!select_player`")
			return
		else:
			await ctx.send("Choose the bowler using `c!select_player`")
			return
	if ctx.message.author.id==Batting_team_id:
		return
	x=x["Score_card"]
	a=x["Overs"].split(".")
	a=a[0]
	c=x["Maximum_overs"].split(".")
	c=c[0]
	#outcomes=[1]
	outcomes=[1, 4, 2, 2, 2, 6, 'no-ball', 3, 2, 2, 2, 4, 1, 1, 2, 1, 2, 1, 'wicket', 1, 3, 1, 'wicket', 0, 2, 'no-ball', 1, 2, 2, 'wicket', 0, 1, 'wicket', 'wide', 2, 1, 'no-ball', 2, 4, 2, 'wide', 6, 1, 3, 0, 1, 3, 2, 'no-ball', 1, 2, 1, 0, 'wicket', 'wide', 3, 2, 6, 1, 4, 1, 3, 'wide', 4, 3, 2, 0, 4, 6, 1, 'wicket', 2, 0, 4, 4, 3, 'wide', 2, 0, 0, 1, 'wide', 1, 1]
	if a=='0':
		#outcomes=[1]
		outcomes=[1, 4, 'wicket', 4, 'wide', 2, 1, 0, 'no-ball', 0, 3, 1, 1, 2, 6, 1, 1, 4, 0, 4, 'wicket', 0, 4, 'no-ball', 0, 4, 'wide', 6, 6, 4, 6, 3, 2, 'wicket', 1, 4, 'wicket', 4, 2, 0, 2, 3, 2, 4, 6, 1, 1, 'wicket', 0, 'wicket', 4, 0, 'wide', 4, 6, 0, 4, 3, 4, 6, 0, 6, 1, 2, 'wide', 2, 2, 2, 4]
	elif a==str(int(c)-1) and a!='0':
		#outcomes=[1]
		outcomes=[0, 2, 'wicket', 1, 'wicket', 'wicket', 0, 4, 1, 6, 4, 4, 4, 1, 6, 0, 2, 6, 1, 0, 1, 1, 'no-ball', 1, 4, 1, 'wide', 0, 1, 4, 'wicket', 'no-ball', 'no-ball', 4, 'wicket', 0, 0, 3, 3, 3, 'wide', 4, 4, 0, 0, 'wicket', 6, 2, 4, 2, 4, 'wide', 2, 'no-ball', 4, 2, 6, 4, 2, 2, 2, 4, 6, 4, 6, 3, 2, 6, 0, 'wide', 1]
	random.shuffle(outcomes)
	o=random.choice(outcomes)
	if o==0:
		img="https://thumbs.gfycat.com/CrazyRigidGyrfalcon-size_restricted.gif"
		txt="Well bowled! no runs came off that ball"
	if o==1:
		img='https://media.giphy.com/media/3oh6e1cdNdVLlfUXpE/giphy.gif'
		txt='Straight to the fielder for a single!'
	if o==2:
		img='https://media.giphy.com/media/pPd3Tzuc34UpJJvK2F/giphy.gif'
		txt='Nudged into the gap for a double.'
	if o==3:
		img='https://media1.giphy.com/media/NRtZEyZjbLgr0BJ4B8/giphy.gif'
		txt="They turned that into 3, that's very good running"
	if o==4:
		img='https://media.tenor.com/images/0b12eaa6835a3fb204ea4965f728613c/tenor.gif'
		txt='Smashed into the gap for a FOUR'
	if o==6:
		img='https://media0.giphy.com/media/MuHNNsIf3CzcTsdpcv/giphy.gif?cid=19f5b51a7fde06336ea661ea8b0c5339572716c561abaef1&rid=giphy.gif'
		txt="The fielder can do nothing but watch the ball sail over his head, its a SIX!"
	if o=='no-ball':
		z=[2, 2, 3, 2, 0, 2, 1, 0, 2, 2, 3,'wicket', 2, 3, 1, 1, 4, 1, 1, 0, 3, 6, 1, 0, 2, 1, 0, 2, 1, 'wicket',3, 2, 3, 1, 4, 0, 3, 4, 3, 1, 2, 1, 2, 2, 4, 2, 0, 1, 4, 2, 1, 1, 2, 3, 2, 1,'wicket', 0, 2, 2, 0, 2, 0, 0, 6, 3, 2, 3, 6, 3, 1, 0, 1, 2, 0, 3, 0, 4, 4, 0, 2, 1, 4, 4, 1, 1, 1, 2, 1, 6, 2, 1, 0, 0, 1, 0, 0, 1, 3, 6, 3, 0]
		z=random.choice(z)
		if z==0:
			imge="https://thumbs.gfycat.com/CrazyRigidGyrfalcon-size_restricted.gif"
			txte="Well bowled! no runs came off that ball"
		if z==1:
			imge='https://media.giphy.com/media/3oh6e1cdNdVLlfUXpE/giphy.gif'
			txte='Straight to the fielder for a single!'
		if z==2:
			imge='https://media.giphy.com/media/pPd3Tzuc34UpJJvK2F/giphy.gif'
			txte='Nudged into the gap for a double.'
		if z==3:
			imge='https://media1.giphy.com/media/NRtZEyZjbLgr0BJ4B8/giphy.gif'
			txte="They turned that into 3, that's very good running"
		if z==4:
			imge='https://media.tenor.com/images/0b12eaa6835a3fb204ea4965f728613c/tenor.gif'
			txte='Smashed into the gap for a FOUR'
		if z==6:
			imge='https://media0.giphy.com/media/MuHNNsIf3CzcTsdpcv/giphy.gif?cid=19f5b51a7fde06336ea661ea8b0c5339572716c561abaef1&rid=giphy.gif'
			txte="The fielder can do nothing but watch the ball sail over his head, its a SIX!"
		if z=='wicket':
			img='https://media.discordapp.net/attachments/549222632873000980/705010813517299712/videotogif_2020.04.29_19.00.44.gif?width=403&height=403'
			txt=["Bullseye! The bowler doesn't miss the stumps this time","The fielder pulls out a blinder!!"]
		embed=discord.Embed(title=txte)
		embed.set_image(url=f'{imge}')
		await ctx.send(embed=embed)
		#img='https://media.discordapp.net/attachments/549222632873000980/705001910490628146/PicsArt_04-29-06.25.25.gif?width=425&height=425'
		txt="The bowler over-stepped this time, it's a no ball"
	if o=='wide':
		img='https://media.discordapp.net/attachments/549222632873000980/704999410580324412/PicsArt_04-29-06.15.40.gif?width=425&height=425'
		txt="Extra runs for the batting team, it's a wide"
	if o=='wicket':
		img='https://media.discordapp.net/attachments/549222632873000980/705010813517299712/videotogif_2020.04.29_19.00.44.gif?width=403&height=403'
		txt=["Bullseye! The bowler doesn't miss the stumps this time","The fielder pulls out a blinder!!","And a pretty good throw from the fielder yielded them a wicket"]
		txt=random.choice(txt)
	embed=discord.Embed(title=txt)
	if img==None:
		await ctx.send(embed=embed)
	else:
		embed.set_image(url=f'{img}')
		await ctx.send(embed=embed)
	d={0:0,1:1,2:2,3:3,4:4,6:6,'no-ball':1,'wide':1,'wicket':0}
	extras=["no-ball","wide"]
	last=None
	#score
	x["Score"]=int(x["Score"])+d[o]
	Bowling_team["Bowling"][Bowling_team["Current_bowling"][0]]["runs"]+=d[o]
	if o in extras:
		pass
	else:
		Batting_team["Batting"][Batting_team["Current_batting"][0]]["runs"]+=d[o]
		Batting_team["Batting"][Batting_team["Current_batting"][0]]["balls_faced"]+=1
		if d[o]%2!=0:
			Batting_team["Current_batting"].reverse()
	if z==None:
		pass
	else:
		Bowling_team["Bowling"][Bowling_team["Current_bowling"][0]]["runs"]+=d[o]
		x["Score"]=int(x["Score"])+d[z]
		if z not in extras:
			Batting_team["Batting"][Batting_team["Current_batting"][0]]["runs"]+=d[z]
			Batting_team["Batting"][Batting_team["Current_batting"][0]]["balls_faced"]+=1
			if d[z]%2!=0:
				Batting_team["Current_batting"].reverse()
	if int(x["Score"])>=int(x["Target"]) and int(x["Target"])!=0:
		last=f"GG both teams, well played! "+Batting_team_name+" won over "+Bowling_team_name+" by "+str(10-int(x["Wickets"]))+" wickets"
		embed=discord.Embed(title="Scoreboard",description=f"{last}\n\n**First Innings Score :**\nScore : {x['First_innings_score']}\n\n**Second Innings Score :**\nScore : {x['Score']}/{x['Wickets']}")
		await ctx.send(embed=embed)
		db_collection.delete_one({"Now_batting": original_data["Now_batting"]})
		p=db1_collection.find_one({})
		p=p["ids"]
		p.pop(p.index(Batting_team_id))
		p.pop(p.index(Bowling_team_id))
		db1_collection.update_one({},{"$set":{"ids": p}})
		team1_profile=db2_collection.find_one({"id": Batting_team_id})
		team2_profile=db2_collection.find_one({"id": Bowling_team_id})
		
		#team1
		team1_profile["current_streak"]+=1
		if team1_profile["current_streak"]>team1_profile["highest_streak"]:
			team1_profile["highest_streak"]=team1_profile["current_streak"]
		team1_profile["won"]+=1
		team1_profile["matches_played"]+=1
		team1_profile["recent_results"].append("W")
		if len(team1_profile["recent_results"])>5:
			team1_profile["recent_results"].pop(0)
		#team2
		team2_profile["current_streak"]=0
		team2_profile["lost"]+=1
		team2_profile["matches_played"]+=1
		team2_profile["recent_results"].append("L")
		if len(team2_profile["recent_results"])>5:
			team2_profile["recent_results"].pop(0)

		db2_collection.update_one({"id": team1_profile["id"]},{"$set":{"now_match":"","matches_played":team1_profile["matches_played"],"won":team1_profile["won"],"highest_streak":team1_profile["highest_streak"],"current_streak": team1_profile["current_streak"],"recent_results": team1_profile["recent_results"]}})
		db2_collection.update_one({"id": team2_profile["id"]},{"$set":{"now_match":"","matches_played":team2_profile["matches_played"],"lost":team2_profile["lost"],"current_streak": team2_profile["current_streak"],"recent_results": team2_profile["recent_results"]}})
		return
	if o=='wicket':
		if x["Last_ball"]=='no-ball':
			last="A total waste, coz its a free hit"
		else:
			Bowling_team["Bowling"][Bowling_team["Current_bowling"][0]]["wickets"]+=1
			Batting_team["Batsmen_out"].append(Batting_team["Current_batting"].pop(0))
			x["Wickets"]=int(x["Wickets"])+1
			if x["Wickets"]==original_data["Maximum_wickets"]:
				if x["Target"]==0:
					x["Target"]=int(x["Score"])+1
					db_collection.update_one({"Now_batting": Batting_team_id},{"$set":{"This_over": "","Score_card":{"Target": x["Target"],
								"Overs": "0.0",
								"Maximum_overs": x["Maximum_overs"],
								"Last_ball": "0",
								"Score": 0,
								"Wickets": 0,
								"Toss": x["Toss"],
								"First_innings_score": str(x['Target']-1)+"/"+str(x['Wickets'])},"Now_batting": Bowling_team_id}})
					embed=discord.Embed(title=f"Well played {Batting_team_name}, {Bowling_team_name} your Target is {x['Target']} runs")
					await ctx.send(embed=embed)
					return
				elif (x["Target"])>int(x["Score"]):
					last="GG both teams, well played! "+Bowling_team_name+" won over Team "+Batting_team_name+" by "+str(int(x["Target"])-int(x["Score"]))+" runs"
					embed=discord.Embed(title="Scoreboard",description=f"{last}\n\n**First Innings Score :**\nScore : {x['First_innings_score']}\n\n**Second Innings Score :**\nScore : {x['Score']}/{x['Wickets']}")
					await ctx.send(embed=embed)
					db_collection.delete_one({"Now_batting": original_data["Now_batting"]})
					p=db1_collection.find_one({})
					p=p["ids"]
					p.pop(p.index(Batting_team_id))
					p.pop(p.index(Bowling_team_id))
					db1_collection.update_one({},{"$set":{"ids": p}})
					team2_profile=db2_collection.find_one({"id": Batting_team_id})
					team1_profile=db2_collection.find_one({"id": Bowling_team_id})
				
					#team1
					team1_profile["current_streak"]+=1
					if team1_profile["current_streak"]>team1_profile["highest_streak"]:
						team1_profile["highest_streak"]=team1_profile["current_streak"]
					team1_profile["won"]+=1
					team1_profile["matches_played"]+=1
					team1_profile["recent_results"].append("W")
					if len(team1_profile["recent_results"])>5:
						team1_profile["recent_results"].pop(0)
					#team2
					team2_profile["current_streak"]=0
					team2_profile["lost"]+=1
					team2_profile["matches_played"]+=1
					team2_profile["recent_results"].append("L")
					if len(team2_profile["recent_results"])>5:
						team2_profile["recent_results"].pop(0)
			
					db2_collection.update_one({"id": team1_profile["id"]},{"$set":{"now_match":"","matches_played":team1_profile["matches_played"],"won":team1_profile["won"],"highest_streak":team1_profile["highest_streak"],"current_streak": team1_profile["current_streak"],"recent_results": team1_profile["recent_results"]}})
					db2_collection.update_one({"id": team2_profile["id"]},{"$set":{"now_match":"","matches_played":team2_profile["matches_played"],"lost":team2_profile["lost"],"current_streak": team2_profile["current_streak"],"recent_results": team2_profile["recent_results"]}})
					return
				else:
					last="GG both teams, well played! Since it turned out to be no one's, lets go for a super-over..."+Batting_team_name+" will bat first"
					db_collection.update_one({"Now_batting": Batting_team_id},{"$set":{"Maximum_wickets":2,"This_over": "","Maximum_overs":1,"Score_card":{"Target": 0,
								"Overs": "0.0",
								"Maximum_overs": "1.0",
								"Last_ball": "0",
								"Score": 0,
								"Wickets": 0,
								"Toss": x["Toss"],
								"First_innings_score": "0"},"Team1_data":{
																	"Lineup": original_data["Team1_data"]["Lineup"],
																	"Batting": {},
																	"Bowling": {},
																	"Current_batting": [],
																	"Current_bowling": [],
																	"Previous_bowler": [],
																	"Batsmen_out": []
																},
																"Team2_data":{
																	"Lineup": original_data["Team2_data"]["Lineup"],
																	"Batting": {},
																	"Bowling": {},
																	"Current_batting": [],
																	"Current_bowling": [],
																	"Previous_bowler": [],
																	"Batsmen_out": []
																}}})
					embed=discord.Embed(title=last)
					await ctx.send(embed=embed)
					return
					
	#prev-ball
	if x["Last_ball"]=='no-ball':
		if o=='wide':
			last="Pull-up ur socks batsman, coz its a freehit"
			x["Last_ball"]='no-ball'
			if o=="wicket":
				This_over+=" "+"0"
			else:
				This_over+=" "+str(o)
		else:
			x["Last_ball"]=str(o)+' free-hit'
			if o=="no-ball":
				This_over+=" "+str(z)+"nb"
			elif o=="wicket":
				This_over+=" "+"W"
			else:
				This_over+=" "+str(o)
	else:
		x["Last_ball"]=str(o)
		if o=="no-ball":
			This_over+=" "+str(z)+"nb"
		elif o=="wicket":
			This_over+=" "+"W"
		else:
			This_over+=" "+str(o)
	original_data["This_over"]=This_over
	#overs
	if o=='no-ball' or o=='wide':
		
		pass
	else:
		temp=x["Overs"].split(".")
		temp[1]=str(int(temp[1])+1)
		Bowling_team["Bowling"][Bowling_team["Current_bowling"][0]]["balls_thrown"]+=1
		
		if temp[1]=='6':
			temp[0]=str(int(temp[0])+1)
			temp[1]=str(0)
			Bowling_team["Previous_bowler"]=Bowling_team["Current_bowling"].pop(0)
			Batting_team["Current_batting"].reverse()
			original_data["This_over"]=""
		temp=".".join(temp)
		if temp==x["Maximum_overs"]:
			if x["Target"]==0:
				x["Target"]=int(x["Score"])+1
				embed=discord.Embed(title=f"Well played {Batting_team_name}, {Bowling_team_name} your Target is {x['Target']} runs")
				db_collection.update_one({"Now_batting": Batting_team_id},{"$set":{"This_over": "","Score_card":{"Target": x["Target"],
								"Overs": "0.0",
								"Maximum_overs": x["Maximum_overs"],
								"Last_ball": "0",
								"Score": 0,
								"Wickets": 0,
								"Toss": x["Toss"],
								"First_innings_score": str(x['Target']-1)+"/"+str(x['Wickets'])},"Now_batting":Bowling_team_id}})
				await ctx.send(embed=embed)
				return
			else:
				if int(x["Score"])<int(int(x["Target"])-1):
					last="GG both teams, well played! "+Bowling_team_name+" won over "+Batting_team_name+" by "+str(int(x["Target"])-int(x["Score"])-1)+" runs"
					embed=discord.Embed(title="Scoreboard",description=f"{last}\n\n**First Innings Score :**\nScore : {x['First_innings_score']}\n\n**Second Innings Score :**\nScore : {x['Score']}/{x['Wickets']}")
					await ctx.send(embed=embed)
					db_collection.delete_one({"Now_batting": original_data["Now_batting"]})
					p=db1_collection.find_one({})
					p=p["ids"]
					p.pop(p.index(Batting_team_id))
					p.pop(p.index(Bowling_team_id))
					db1_collection.update_one({},{"$set":{"ids": p}})
					team2_profile=db2_collection.find_one({"id": Batting_team_id})
					team1_profile=db2_collection.find_one({"id": Bowling_team_id})
			
					#team1
					team1_profile["current_streak"]+=1
					if team1_profile["current_streak"]>team1_profile["highest_streak"]:
						team1_profile["highest_streak"]=team1_profile["current_streak"]
					team1_profile["won"]+=1
					team1_profile["matches_played"]+=1
					team1_profile["recent_results"].append("W")
					if len(team1_profile["recent_results"])>5:
						team1_profile["recent_results"].pop(0)
					#team2
					team2_profile["current_streak"]=0
					team2_profile["lost"]+=1
					team2_profile["matches_played"]+=1
					team2_profile["recent_results"].append("L")
					if len(team2_profile["recent_results"])>5:
						team2_profile["recent_results"].pop(0)
					db2_collection.update_one({"id": team1_profile["id"]},{"$set":{"now_match":"","matches_played":team1_profile["matches_played"],"won":team1_profile["won"],"highest_streak":team1_profile["highest_streak"],"current_streak": team1_profile["current_streak"],"recent_results": team1_profile["recent_results"]}})
					db2_collection.update_one({"id": team2_profile["id"]},{"$set":{"now_match":"","matches_played":team2_profile["matches_played"],"lost":team2_profile["lost"],"current_streak": team2_profile["current_streak"],"recent_results": team2_profile["recent_results"]}})
			
					return
				elif int(x["Score"])==int(int(x["Target"])-1):
					last="GG both teams, well played! Since it turned out to be no one's, lets go for a super-over..."+Batting_team_name+" will bat first"
					db_collection.update_one({"Now_batting": Batting_team_id},{"$set":{"Maximum_wickets":2,"This_over": "","Maximum_overs":1,"Score_card":{"Target": 0,
								"Overs": "0.0",
								"Maximum_overs": "1.0",
								"Last_ball": "0",
								"Score": 0,
								"Wickets": 0,
								"Toss": x["Toss"],
								"First_innings_score": "0"},"Team1_data":{
																	"Lineup": original_data["Team1_data"]["Lineup"],
																	"Batting": {},
																	"Bowling": {},
																	"Current_batting": [],
																	"Current_bowling": [],
																	"Previous_bowler": [],
																	"Batsmen_out": []
																},
																"Team2_data":{
																	"Lineup": original_data["Team2_data"]["Lineup"],
																	"Batting": {},
																	"Bowling": {},
																	"Current_batting": [],
																	"Current_bowling": [],
																	"Previous_bowler": [],
																	"Batsmen_out": []
																}}})
					embed=discord.Embed(title=last)
					await ctx.send(embed=embed)
					return
		x["Overs"]=temp		
	if Batting_team_id==original_data["Team1_member_id"]:
		original_data["Team1_data"]["Batting"]=Batting_team["Batting"]
		original_data["Team1_data"]["Current_batting"]=Batting_team["Current_batting"]
		original_data["Team1_data"]["Batsmen_out"]=Batting_team["Batsmen_out"]
		original_data["Team2_data"]["Previous_bowler"]=Bowling_team["Previous_bowler"]
		original_data["Team2_data"]["Bowling"]=Bowling_team["Bowling"]
		original_data["Team2_data"]["Current_bowling"]=Bowling_team["Current_bowling"]
	else:
		original_data["Team2_data"]["Batting"]=Batting_team["Batting"]
		original_data["Team2_data"]["Current_batting"]=Batting_team["Current_batting"]
		original_data["Team2_data"]["Batsmen_out"]=Batting_team["Batsmen_out"]
		original_data["Team1_data"]["Previous_bowler"]=Bowling_team["Previous_bowler"]
		original_data["Team1_data"]["Bowling"]=Bowling_team["Bowling"]
		original_data["Team1_data"]["Current_bowling"]=Bowling_team["Current_bowling"]
	db_collection.update_one({"Now_batting": Batting_team_id},{"$set":{"Score_card":{"Target": x["Target"],
								"Overs": x["Overs"],
								"Maximum_overs": x["Maximum_overs"],
								"Last_ball": x["Last_ball"],
								"Score": x["Score"],
								"Wickets": x["Wickets"],
								"Toss": x["Toss"],
								"First_innings_score": x["First_innings_score"]},"Team1_data":{
																	"Lineup": original_data["Team1_data"]["Lineup"],
																	"Batting": original_data["Team1_data"]['Batting'],
																	"Bowling": original_data["Team1_data"]['Bowling'],
																	"Current_batting": original_data["Team1_data"]['Current_batting'],
																	"Current_bowling": original_data["Team1_data"]['Current_bowling'],
																	"Previous_bowler": original_data["Team1_data"]['Previous_bowler'],
																	"Batsmen_out": original_data["Team1_data"]['Batsmen_out']
																},
																"Team2_data":{
																	"Lineup": original_data["Team2_data"]["Lineup"],
																	"Batting": original_data["Team2_data"]['Batting'],
																	"Bowling": original_data["Team2_data"]['Bowling'],
																	"Current_batting": original_data["Team2_data"]['Current_batting'],
																	"Current_bowling": original_data["Team2_data"]['Current_bowling'],
																	"Previous_bowler": original_data["Team2_data"]['Previous_bowler'],
																	"Batsmen_out": original_data["Team2_data"]['Batsmen_out']
																},"This_over": original_data["This_over"]}})
	score=""
	if x["Target"]==0:
		score+="Score: "+str(x["Score"])+"/"+str(x["Wickets"])+"\nOvers: "+x["Overs"]+"/"+x["Maximum_overs"]
	else:
		t=x["Overs"].split(".")
		b=x["Maximum_overs"].split(".")
		b=int(b[0])-1
		if t[1]=='0':
			t[1]=int(t[1])
		else:
			t[1]=6-int(t[1])
		t[0]=b-int(t[0])
		if t[1]==0:
			t[1]=6
		total=t[0]*6+t[1]
		score+="Score: "+str(x["Score"])+"/"+str(x["Wickets"])+"\nOvers: "+x["Overs"]+"/"+x["Maximum_overs"]+"\nNeed "+str(int(x["Target"])-int(x["Score"])) +" from "+str(total)
		if total==1:
			score+=" ball"
		else:
			score+=" balls"
	if o=='no-ball':
		last="Pull-up ur socks batsman, coz its a freehit"
	'''if last==None:
		embed=discord.Embed(title=f"{score}")
	else:
		embed=discord.Embed(title=f"{last}\n{score}")
	await ctx.send(embed=embed)'''
	overs=None
	if len(Bowling_team['Current_bowling'])==0:
		pass
	else:
		overs=str(int(math.floor(Bowling_team['Bowling'][Bowling_team['Current_bowling'][0]]["balls_thrown"]/6)))+"."+str(Bowling_team['Bowling'][Bowling_team['Current_bowling'][0]]["balls_thrown"]%6)
	if last==None:
		if len(Batting_team['Current_batting'])!=1:
			if overs==None:
				await ctx.send(f"```{score}\n\n{Batting_team['Current_batting'][0]} : {Batting_team['Batting'][Batting_team['Current_batting'][0]]['runs']}({Batting_team['Batting'][Batting_team['Current_batting'][0]]['balls_faced']})\n{Batting_team['Current_batting'][1]} : {Batting_team['Batting'][Batting_team['Current_batting'][1]]['runs']}({Batting_team['Batting'][Batting_team['Current_batting'][1]]['balls_faced']})\n\nThis Over: {This_over}```")
			else:
				await ctx.send(f"```{score}\n\n{Batting_team['Current_batting'][0]} : {Batting_team['Batting'][Batting_team['Current_batting'][0]]['runs']}({Batting_team['Batting'][Batting_team['Current_batting'][0]]['balls_faced']})\n{Batting_team['Current_batting'][1]} : {Batting_team['Batting'][Batting_team['Current_batting'][1]]['runs']}({Batting_team['Batting'][Batting_team['Current_batting'][1]]['balls_faced']})\n\nThis Over: {This_over}\n\n{Bowling_team['Current_bowling'][0]}: {Bowling_team['Bowling'][Bowling_team['Current_bowling'][0]]['runs']}/{Bowling_team['Bowling'][Bowling_team['Current_bowling'][0]]['wickets']} ({overs})```")
		else:
			if overs==None:
				await ctx.send(f"```{score}\n\n{Batting_team['Current_batting'][0]} : {Batting_team['Batting'][Batting_team['Current_batting'][0]]['runs']}({Batting_team['Batting'][Batting_team['Current_batting'][0]]['balls_faced']})*\n\nThis Over: {This_over}```")
			else:
				await ctx.send(f"```{score}\n\n{Batting_team['Current_batting'][0]} : {Batting_team['Batting'][Batting_team['Current_batting'][0]]['runs']}({Batting_team['Batting'][Batting_team['Current_batting'][0]]['balls_faced']})*\n\nThis Over: {This_over}\n\n{Bowling_team['Current_bowling'][0]}: {Bowling_team['Bowling'][Bowling_team['Current_bowling'][0]]['runs']}/{Bowling_team['Bowling'][Bowling_team['Current_bowling'][0]]['wickets']} ({overs})```")

		#embed=discord.Embed(title=f"{score}\n{Batting_team['Current_batting'][0]} : {Batting_team['Batting'][Batting_team['Current_batting'][0]]['runs']}({Batting_team['Batting'][Batting_team['Current_batting'][0]]['balls_faced']})\n{Batting_team['Current_batting'][1]} : {Batting_team['Batting'][Batting_team['Current_batting'][1]]['runs']}({Batting_team['Batting'][Batting_team['Current_batting'][1]]['balls_faced']})\nThis Over: {This_over}")
	else:
		if overs==None:
			await ctx.send(f'```{last}\n\n{score}\n\n{Batting_team["Current_batting"][0]} : {Batting_team["Batting"][Batting_team["Current_batting"][0]]["runs"]}({Batting_team["Batting"][Batting_team["Current_batting"][0]]["balls_faced"]})*\n{Batting_team["Current_batting"][1]} : {Batting_team["Batting"][Batting_team["Current_batting"][1]]["runs"]}({Batting_team["Batting"][Batting_team["Current_batting"][1]]["balls_faced"]})\n\nThis Over: {This_over}```')
		else:
			await ctx.send(f'```{last}\n\n{score}\n\n{Batting_team["Current_batting"][0]} : {Batting_team["Batting"][Batting_team["Current_batting"][0]]["runs"]}({Batting_team["Batting"][Batting_team["Current_batting"][0]]["balls_faced"]})*\n{Batting_team["Current_batting"][1]} : {Batting_team["Batting"][Batting_team["Current_batting"][1]]["runs"]}({Batting_team["Batting"][Batting_team["Current_batting"][1]]["balls_faced"]})\n\nThis Over: {This_over}\n\n{Bowling_team["Current_bowling"][0]}: {Bowling_team["Bowling"][Bowling_team["Current_bowling"][0]]["runs"]}/{Bowling_team["Bowling"][Bowling_team["Current_bowling"][0]]["wickets"]} ({overs})```')
		#embed=discord.Embed(title=f'{last}\n\n{score}\n\n{Batting_team["Current_batting"][0]} : {Batting_team["Batting"][Batting_team["Current_batting"][0]]["runs"]}({Batting_team["Batting"][Batting_team["Current_batting"][0]]["balls_faced"]})\n{Batting_team["Current_batting"][1]} : {Batting_team["Batting"][Batting_team["Current_batting"][1]]["runs"]}({Batting_team["Batting"][Batting_team["Current_batting"][1]]["balls_faced"]})\n\nThis Over: {This_over}')
	#await ctx.send(embed=embed)
	
	
@bot.command(aliases=['sb','scorecard'])
async def scoreboard(ctx):
	x=db_collection.find_one({"Team1_member_id": ctx.message.author.id})
	if x==None:
		x=db_collection.find_one({"Team2_member_id": ctx.message.author.id})
		if x==None:
			return
		else:
			x=x["Score_card"]
			if x["Target"]==0:
				embed=discord.Embed(title="Scoreboard",description=f"**First Innings Score :**\nScore : {x['Score']}/{x['Wickets']}\nOvers : {x['Overs']}/{x['Maximum_overs']}")
				await ctx.send(embed=embed)
				return
			else:
				embed=discord.Embed(title="Scoreboard",description=f"**Target :** {x['Target']}\n**Overs :** {x['Overs']}/{x['Maximum_overs']}\n\n**First Innings Score :**\nScore : {x['First_innings_score']}\n\n**Second Innings Score :**\nScore : {x['Score']}/{x['Wickets']}")
				await ctx.send(embed=embed)
				return
	else:
		x=x["Score_card"]
		if x["Target"]==0:
			embed=discord.Embed(title="Scoreboard",description=f"**First Innings Score :**\nScore : {x['Score']}/{x['Wickets']}\nOvers : {x['Overs']}/{x['Maximum_overs']}")
			await ctx.send(embed=embed)
			return
		else:
			embed=discord.Embed(title="Scoreboard",description=f"**Target :** {x['Target']}\n**Overs :** {x['Overs']}/{x['Maximum_overs']}\n\n**First Innings Score :**\nScore : {x['First_innings_score']}\n\n**Second Innings Score :**\nScore : {x['Score']}/{x['Wickets']}")
			await ctx.send(embed=embed)
			return
@bot.command(aliases=["e"])
async def end(ctx):
	x=db_collection.find_one({"Team1_member_id": ctx.message.author.id})
	try:
		if x==None:
			x=db_collection.find_one({"Team2_member_id": ctx.message.author.id})
			if x==None:
				await ctx.send("No matches are running")
				return
			else:
				xy=db1_collection.find_one()
				team1_member=None
				for i in bot.guilds:
					for j in i.members:
						if x["Team1_member_id"]==j.id:
							team1_member=j
							break
					if team1_member!=None:
						break
				team2_member=ctx.message.author
				db2_collection.update_one({"id": team2_member.id},{"$set":{"now_match" :""}})
				db2_collection.update_one({"id": x["Team1_member_id"]},{"$set":{"now_match" :""}})
				if team1_member==None:
					team1_member.id=x["Team1_member_id"]
					db_collection.delete_one({"Team2_member_id":team2_member.id})
					xy["ids"].pop(xy["ids"].index(team1_member.id))
					xy["ids"].pop(xy["ids"].index(team2_member.id))
					db1_collection.update_one({},{"$set":{"ids":x["ids"]}})
					await ctx.send("Match abandoned successfully")
					return				
				db_collection.delete_one({"Team2_member_id":team2_member.id})
				xy["ids"].pop(xy["ids"].index(team1_member.id))
				xy["ids"].pop(xy["ids"].index(team2_member.id))
				db1_collection.update_one({},{"$set":{"ids":xy["ids"]}})
				await ctx.send("Match abandoned successfully")
				if team2_member.dm_channel==None:
					await team2_member.create_dm()	
				if team1_member.dm_channel==None:
					await team1_member.create_dm()
				dm1=team2_member.dm_channel
				dm2=team1_member.dm_channel			
				await dm1.send(f"Match between **{team1_member.name}#{team1_member.discriminator}** vs **{team2_member.name}#{team2_member.discriminator}** has been abandoned by {ctx.message.author.name}#{ctx.message.author.discriminator}")
				await dm2.send(f"Match between **{team1_member.name}#{team1_member.discriminator}** vs **{team2_member.name}#{team2_member.discriminator}** has been abandoned by {ctx.message.author.name}#{ctx.message.author.discriminator}")
		else:
			xy=db1_collection.find_one()
			team2_member=None
			for i in bot.guilds:
				for j in i.members:
					if x["Team2_member_id"]==j.id:
						team2_member=j
						break
				if team2_member!=None:
					break
			team1_member=ctx.message.author
			db2_collection.update_one({"id": team1_member.id},{"$set":{"now_match" :""}})
			db2_collection.update_one({"id": x["Team2_member_id"]},{"$set":{"now_match" :""}})
			if team2_member==None:
				team2_member.id=x["Team2_member_id"]
				
				db_collection.delete_one({"Team1_member_id":team1_member.id})
				xy["ids"].pop(xy["ids"].index(team1_member.id))
				xy["ids"].pop(xy["ids"].index(team2_member.id))
				db1_collection.update_one({},{"$set":{"ids":x["ids"]}})
				await ctx.send("Match abandoned successfully")
				return
			
			db_collection.delete_one({"Team1_member_id":team1_member.id})
			xy["ids"].pop(xy["ids"].index(team1_member.id))
			xy["ids"].pop(xy["ids"].index(team2_member.id))
			db1_collection.update_one({},{"$set":{"ids":xy["ids"]}})
			await ctx.send("Match abandoned successfully")

			if team2_member.dm_channel==None:
				await team2_member.create_dm()
			if team1_member.dm_channel==None:
				await team1_member.create_dm()
			dm1=team2_member.dm_channel
			dm2=team1_member.dm_channel
			await dm1.send(f"Match between **{team1_member.name}#{team1_member.discriminator}** vs **{team2_member.name}#{team2_member.discriminator}** has been abandoned by {ctx.message.author.name}#{ctx.message.author.discriminator}")
			await dm2.send(f"Match between **{team1_member.name}#{team1_member.discriminator}** vs **{team2_member.name}#{team2_member.discriminator}** has been abandoned by {ctx.message.author.name}#{ctx.message.author.discriminator}")
		
	except:
		pass
@bot.command(aliases=["ca","start","register"])
async def create_account(ctx):
	h=db2_collection.find_one({"id":ctx.author.id})
	if h!=None:
		await ctx.send("Seems like you have an account already, type `c!profile` to check profile")
		return
	guild=0
	for i in bot.guilds:
		if i.id==723905142646243442:
			guild=i
			break
	if ctx.author not in guild.members:
		await ctx.send("You need be a member of the official server to create an account. You can join get the server link by using `c!server` command")
		return
	data={
		"about": "I am a cricket lover!",
		"id": ctx.message.author.id,
		"matches_played": 0,
		"won": 0,
		"lost": 0,
		"highest_streak": 0,
		"current_streak": 0,
		"recent_results": [],
		"now_match": ""
	}
	db2_collection.insert_one(data)
	await ctx.send("Account created successfully!\nType `c!profile` to check the profile")
@bot.command(aliases=["about"])
async def profile(ctx,user:discord.Member=None):
	if user==None:
		User=ctx.message.author
	else:
		User=user
	x=db2_collection.find_one({"id": User.id})
	if x==None:
		if user==None:
			await ctx.send("Create an account by typing `c!register`")
			return
		else:
			await ctx.send(f"Looks like {User.name} doesnt have an account")
	else:
		embed=discord.Embed()
		embed.set_thumbnail(url=f"{User.avatar_url}")
		embed.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator}",icon_url=f"{ctx.author.avatar_url}")
		embed.add_field(name="About",value=f"{x['about']}",inline=False)
		embed.add_field(name="Matches played",value=f"{x['matches_played']}",inline=False)
		embed.add_field(name="Matches won",value=f"{x['won']}",inline=False)
		embed.add_field(name="Matches lost",value=f"{x['lost']}",inline=False)
		if x["matches_played"]==0:
			win=0
		else:
			win=(x['won']/x["matches_played"])*100
		
		embed.add_field(name="Win percentage",value="{:.2f}%".format(win),inline=False)
		if len(x['recent_results'])==0:
			rs="-"
		else:
			rs=' '.join(x['recent_results'])
		embed.add_field(name="Recent results",value=rs)
		embed.set_footer(text=f"Current streak: {x['current_streak']}  Highest streak: {x['highest_streak']}")
		await ctx.send(embed=embed)
@bot.command(aliases=["change_about"])
async def set(ctx,key=None,*,about=None):
	if key==None:
		return
	if key.lower()!="about":
		return
	if about==None:
		return
	x=db2_collection.find_one({"id":ctx.message.author.id})
	if x==None:
		return
	else:
		db2_collection.update_one({"id":ctx.author.id},{"$set":{"about":about}})
		await ctx.send(f"Changed your about to '{about}'")
@bot.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.CommandOnCooldown):
		message=await ctx.send(error)
		await asyncio.sleep(1)
		await message.delete()
bot.run(os.getenv("BOT_TOKEN"))
