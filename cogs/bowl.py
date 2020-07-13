import discord 
import asyncio
import random
from discord.ext import commands
import os
import datetime
import pymongo
import json
import math
db_client=pymongo.MongoClient(os.getenv("DB_URL"))
db1_client=pymongo.MongoClient(os.getenv("DB2_URL"))
db_name=db1_client["Challenge"]
db_collection=db_name['Data']
db1_name=db1_client['Running_matches']
db1_collection=db1_name['data']
db2_name=db_client["about"]
db2_collection=db2_name["data"]
db4_name=db_client["Logs"]
db4_collection = db4_name["Channels"]
class bowl(commands.Cog):
	def __init__(self,bot):
        	self.bot=bot
	@commands.command(aliases=["b"])
	@commands.guild_only()
	@commands.cooldown(1, 4, commands.BucketType.user)
	async def bowl(self,ctx):
		alert=None
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
		v=x["Overs"].split(".")
		a=v[0]
		if (v[1]=='0' and x["Last_ball"]=="wicket") and original_data["This_over"]=="":
			Batting_team["Current_batting"].reverse()
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
			Bowling_team["Bowling"][Bowling_team["Current_bowling"][0]]["runs"]+=d[z]
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
			u=db4_collection.find_one()
			if str(ctx.message.guild.id) in u:
				chnl=self.bot.get_channel(x["str(ctx.message.guild.id)"])
				if chnl!=None:
					last=f"GG both teams, well played! **"+team2_profile['now_match']+"** won over **"+team1_profile['now_match']+"** by "+str(10-int(x["Wickets"]))+" wickets"
					embed=discord.Embed(title="Scoreboard",description=f"{last}\n\n**First Innings Score :**\nScore : {x['First_innings_score']}\n\n**Second Innings Score :**\nScore : {x['Score']}/{x['Wickets']}")
					await chnl.send(embed=embed)
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
			team1_profile["Credits"]+=750+(team1_profile["current_streak"]-1)*100+(10-int(x["Wickets"]))*75
			team2_profile["Credits"]+=750
			db2_collection.update_one({"id": team1_profile["id"]},{"$set":{"now_match":"","matches_played":team1_profile["matches_played"],"won":team1_profile["won"],"highest_streak":team1_profile["highest_streak"],"current_streak": team1_profile["current_streak"],"recent_results": team1_profile["recent_results"],"Credits": team1_profile["Credits"],"winning_percentage": round((team1_profile["won"]/team1_profile["matches_played"])*100,4)}})
			db2_collection.update_one({"id": team2_profile["id"]},{"$set":{"now_match":"","matches_played":team2_profile["matches_played"],"lost":team2_profile["lost"],"current_streak": team2_profile["current_streak"],"recent_results": team2_profile["recent_results"],"Credits": team2_profile["Credits"],"winning_percentage": round((team2_profile["won"]/team2_profile["matches_played"])*100,4)}})
			return
		if o=='wicket':
			if x["Last_ball"]=='no-ball':
				last="A total waste, coz its a free hit"
			else:
				Bowling_team["Bowling"][Bowling_team["Current_bowling"][0]]["wickets"]+=1
				Batting_team["Batsmen_out"].append(Batting_team["Current_batting"].pop(0))
				alert="Select batsman using `c!sp <number>`"
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
						u=db4_collection.find_one()
						if str(ctx.message.guild.id) in u:
							chnl=self.bot.get_channel(x["str(ctx.message.guild.id)"])
							if chnl!=None:
								last="GG both teams, well played! **"+team2_profile["now_match"]+"** won over **"+team2_profile["now_match"]+"** by "+str(int(x["Target"])-int(x["Score"]))+" runs"
								embed=discord.Embed(title="Scoreboard",description=f"{last}\n\n**First Innings Score :**\nScore : {x['First_innings_score']}\n\n**Second Innings Score :**\nScore : {x['Score']}/{x['Wickets']}")
								await chnl.send(embed=embed)
							
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
						team1_profile["Credits"]+=750+(team1_profile["current_streak"]-1)*100+(int(x["Target"])-int(x["Score"]))*25
						team2_profile["Credits"]+=750
						db2_collection.update_one({"id": team1_profile["id"]},{"$set":{"Credits": team1_profile["Credits"],"now_match":"","matches_played":team1_profile["matches_played"],"won":team1_profile["won"],"highest_streak":team1_profile["highest_streak"],"current_streak": team1_profile["current_streak"],"recent_results": team1_profile["recent_results"],"winning_percentage": round((team1_profile["won"]/team1_profile["matches_played"])*100,4)}})
						db2_collection.update_one({"id": team2_profile["id"]},{"$set":{"Credits": team2_profile["Credits"],"now_match":"","matches_played":team2_profile["matches_played"],"lost":team2_profile["lost"],"current_streak": team2_profile["current_streak"],"recent_results": team2_profile["recent_results"],"winning_percentage": round((team2_profile["won"]/team2_profile["matches_played"])*100,4)}})
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
				alert="Select bowler using `c!sp <number>`"
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
						u=db4_collection.find_one()
						if str(ctx.message.guild.id) in u:
							chnl=self.bot.get_channel(x["str(ctx.message.guild.id)"])
							if chnl!=None:
								last="GG both teams, well played! **"+team2_profile["now_match"]+"** won over **"+team2_profile["now_match"]+"** by "+str(int(x["Target"])-int(x["Score"]))+" runs"
								embed=discord.Embed(title="Scoreboard",description=f"{last}\n\n**First Innings Score :**\nScore : {x['First_innings_score']}\n\n**Second Innings Score :**\nScore : {x['Score']}/{x['Wickets']}")
								await chnl.send(embed=embed)
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
						team1_profile["Credits"]+=750+(team1_profile["current_streak"]-1)*100+(int(x["Target"])-int(x["Score"])-1)*25
						team2_profile["Credits"]+=750
						db2_collection.update_one({"id": team1_profile["id"]},{"$set":{"Credits": team1_profile["Credits"],"now_match":"","matches_played":team1_profile["matches_played"],"won":team1_profile["won"],"highest_streak":team1_profile["highest_streak"],"current_streak": team1_profile["current_streak"],"recent_results": team1_profile["recent_results"],"winning_percentage": round((team1_profile["won"]/team1_profile["matches_played"])*100,4)}})
						db2_collection.update_one({"id": team2_profile["id"]},{"$set":{"Credits": team2_profile["Credits"],"now_match":"","matches_played":team2_profile["matches_played"],"lost":team2_profile["lost"],"current_streak": team2_profile["current_streak"],"recent_results": team2_profile["recent_results"],"winning_percentage": round((team2_profile["won"]/team2_profile["matches_played"])*100,4)}})
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
					await ctx.send(f"```{score}\n\n{Batting_team['Current_batting'][0]} : {Batting_team['Batting'][Batting_team['Current_batting'][0]]['runs']}({Batting_team['Batting'][Batting_team['Current_batting'][0]]['balls_faced']})*\n{Batting_team['Current_batting'][1]} : {Batting_team['Batting'][Batting_team['Current_batting'][1]]['runs']}({Batting_team['Batting'][Batting_team['Current_batting'][1]]['balls_faced']})\n\nThis Over: {This_over}```")
				else:
					await ctx.send(f"```{score}\n\n{Batting_team['Current_batting'][0]} : {Batting_team['Batting'][Batting_team['Current_batting'][0]]['runs']}({Batting_team['Batting'][Batting_team['Current_batting'][0]]['balls_faced']})*\n{Batting_team['Current_batting'][1]} : {Batting_team['Batting'][Batting_team['Current_batting'][1]]['runs']}({Batting_team['Batting'][Batting_team['Current_batting'][1]]['balls_faced']})\n\nThis Over: {This_over}\n\n{Bowling_team['Current_bowling'][0]}: {Bowling_team['Bowling'][Bowling_team['Current_bowling'][0]]['runs']}/{Bowling_team['Bowling'][Bowling_team['Current_bowling'][0]]['wickets']} ({overs})```")
			else:
				if overs==None:
					await ctx.send(f"```{score}\n\n{Batting_team['Current_batting'][0]} : {Batting_team['Batting'][Batting_team['Current_batting'][0]]['runs']}({Batting_team['Batting'][Batting_team['Current_batting'][0]]['balls_faced']})\n\nThis Over: {This_over}```")
				else:
					await ctx.send(f"```{score}\n\n{Batting_team['Current_batting'][0]} : {Batting_team['Batting'][Batting_team['Current_batting'][0]]['runs']}({Batting_team['Batting'][Batting_team['Current_batting'][0]]['balls_faced']})\n\nThis Over: {This_over}\n\n{Bowling_team['Current_bowling'][0]}: {Bowling_team['Bowling'][Bowling_team['Current_bowling'][0]]['runs']}/{Bowling_team['Bowling'][Bowling_team['Current_bowling'][0]]['wickets']} ({overs})```")

			#embed=discord.Embed(title=f"{score}\n{Batting_team['Current_batting'][0]} : {Batting_team['Batting'][Batting_team['Current_batting'][0]]['runs']}({Batting_team['Batting'][Batting_team['Current_batting'][0]]['balls_faced']})\n{Batting_team['Current_batting'][1]} : {Batting_team['Batting'][Batting_team['Current_batting'][1]]['runs']}({Batting_team['Batting'][Batting_team['Current_batting'][1]]['balls_faced']})\nThis Over: {This_over}")
		else:
			if overs==None:
				await ctx.send(f'```{last}\n\n{score}\n\n{Batting_team["Current_batting"][0]} : {Batting_team["Batting"][Batting_team["Current_batting"][0]]["runs"]}({Batting_team["Batting"][Batting_team["Current_batting"][0]]["balls_faced"]})*\n{Batting_team["Current_batting"][1]} : {Batting_team["Batting"][Batting_team["Current_batting"][1]]["runs"]}({Batting_team["Batting"][Batting_team["Current_batting"][1]]["balls_faced"]})\n\nThis Over: {This_over}```')
			else:
				await ctx.send(f'```{last}\n\n{score}\n\n{Batting_team["Current_batting"][0]} : {Batting_team["Batting"][Batting_team["Current_batting"][0]]["runs"]}({Batting_team["Batting"][Batting_team["Current_batting"][0]]["balls_faced"]})*\n{Batting_team["Current_batting"][1]} : {Batting_team["Batting"][Batting_team["Current_batting"][1]]["runs"]}({Batting_team["Batting"][Batting_team["Current_batting"][1]]["balls_faced"]})\n\nThis Over: {This_over}\n\n{Bowling_team["Current_bowling"][0]}: {Bowling_team["Bowling"][Bowling_team["Current_bowling"][0]]["runs"]}/{Bowling_team["Bowling"][Bowling_team["Current_bowling"][0]]["wickets"]} ({overs})```')
			#embed=discord.Embed(title=f'{last}\n\n{score}\n\n{Batting_team["Current_batting"][0]} : {Batting_team["Batting"][Batting_team["Current_batting"][0]]["runs"]}({Batting_team["Batting"][Batting_team["Current_batting"][0]]["balls_faced"]})\n{Batting_team["Current_batting"][1]} : {Batting_team["Batting"][Batting_team["Current_batting"][1]]["runs"]}({Batting_team["Batting"][Batting_team["Current_batting"][1]]["balls_faced"]})\n\nThis Over: {This_over}')
		#await ctx.send(embed=embed)
		if alert==None:
			for i in range(3,0,-1):
				if i==3:
					embed=discord.Embed(title=f"{i}")
					m=await ctx.send(embed=embed)
				else:
					o = await ctx.channel.fetch_message(m.id)
					embed=discord.Embed(title=f"{i}")
					await o.edit(embed=embed)
				await asyncio.sleep(1)
			o = await ctx.channel.fetch_message(m.id)
			embed=discord.Embed(title=f"You can continue bowling the next ball")
			await o.edit(embed=embed)
			await asyncio.sleep(1)
			await o.delete()
		else:
			await ctx.send(alert)
			
def setup(bot):
	bot.add_cog(bowl(bot))
