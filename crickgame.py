import discord 
import asyncio
import random
from discord.ext import commands
import os
import datetime
bot=commands.Bot(command_prefix='.')
bot.remove_command('help')
@bot.event
async def on_ready():
	print("Less go")
@bot.command(aliases=["e"])
async def end(ctx):
	channel=ctx.message.channel
	await channel.edit(topic=None)
	embed=discord.Embed(title="Match Abandoned")
	await ctx.send(embed=embed)
@bot.command(aliases=["t"])
async def toss(ctx):
	
	outcomes=["Heads","Tails"]
	answer=random.choice(outcomes)
	embed=discord.Embed(title='Toss')
	embed.set_image(url="https://i.pinimg.com/originals/d7/49/06/d74906d39a1964e7d07555e7601b06ad.gif")
	message=await ctx.send(embed=embed)
	await asyncio.sleep(4)	
	embed=discord.Embed(title=f'Oh! Its a {answer}')
	await message.edit(embed=embed)
@bot.command(aliases=["b"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def bowl(ctx):
	
	channel=ctx.message.channel
	topic=channel.topic
	if topic==None or topic=="":
		embed=discord.Embed(title="Details not given\nType `.so <number>` to set overs")
		await channel.send(embed=embed)
		return
	
	outcomes=[3, 1, 1, 2, 2, 1, 0, 'wide', 0, 4, 1, 4, 2, 0, 3, 2, 1, 1, 'wicket', 4, 4, 2, 3, 0, 2, 1, 4, 4, 4, 2, 3, 'wicket', 2, 3, 1, 2, 'wide', 'wide', 0, 1, 2, 1, 6, 'wide', 1, 2, 0, 3, 4, 2, 'wicket', 1, 4, 1, 2, 4, 0, 1, 'no-ball', 0, 3, 1, 'no-ball', 1, 3, 3, 'wide', 'no-ball', 3, 6, 1, 'no-ball', 3, 2, 0, 1, 2, 2, 0, 2, 'wicket', 6, 2, 6, 2, 3, 2, 'no-ball', 1, 3, 6, 3, 1, 3, 'wicket']
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
		img='https://media.discordapp.net/attachments/549222632873000980/705001910490628146/PicsArt_04-29-06.25.25.gif?width=425&height=425'
		txt="The bowler over-stepped this time, it's a no ball"
	if o=='wide':
		img='https://media.discordapp.net/attachments/549222632873000980/704999410580324412/PicsArt_04-29-06.15.40.gif?width=425&height=425'
		txt="Extra runs for the batting team, it's a wide"
	if o=='wicket':
		img='https://media.discordapp.net/attachments/549222632873000980/705010813517299712/videotogif_2020.04.29_19.00.44.gif?width=403&height=403'
		txt="Bullseye! The bowler doesn't miss the stumps this time"
	embed=discord.Embed(title=txt)
	embed.set_image(url=f'{img}')
	await ctx.send(embed=embed)	
	
	d={0:0,1:1,2:2,3:3,4:4,6:6,'no-ball':1,'wide':1,'wicket':0}
	last=None
	
	
	top=topic.split("\n")
	#score
	top[4]=str(int(top[4])+d[o])
	if int(top[4])>=int(top[0]) and int(top[0])!=0:
		last="GG both teams, well played! Team 2 won over Team 1 by "+str(10-int(top[5]))+" wickets"
		await channel.edit(topic=None)
		embed=discord.Embed(title=last)
		await ctx.send(embed=embed)
		return
	#wickets
	if o=='wicket':
		if top[3]=='no-ball':
			last="A total waste, coz its a free hit"
		else:
			top[5]=str(int(top[5])+1)
			if top[5]=='10':
				if top[0]=='0':
					top[0]=str(int(top[4])+1)
					top[1],top[3],top[4],top[5]='0.0','0','0','0'
					topic="\n".join(top)
					await channel.edit(topic=topic)
					embed=discord.Embed(title=f"Well played Team 1, Team 2 your Target is {top[0]} runs")
					await ctx.send(embed=embed)
					return
				else:
					last="GG both teams, well played! Team 1 won over Team 2 by "+str(int(top[0])-int(top[4]))+" runs"
					await channel.edit(topic=None)
					embed=discord.Embed(title=last)
					await ctx.send(embed=embed)
					return
	#prev-ball
	if top[3]=='no-ball':
		if o=='wide':
			last="Pull-up ur socks batsman, coz its a freehit"
			top[3]='no-ball'
		else:
			top[3]=str(o)+'free-hit'
	else:
		top[3]=str(o)
	
	#overs
	if o=='no-ball' or o=='wide':
		pass
	else:
		temp=top[1].split(".")
		temp[1]=str(int(temp[1])+1)
		if temp[1]=='6':
			temp[0]=str(int(temp[0])+1)
			temp[1]=str(0)
		temp=".".join(temp)
		if temp==top[2]:
			if top[0]=='0':
				top[0]=str(int(top[4])+1)
				top[1],top[3],top[4],top[5]='0.0','0','0','0'
				topic="\n".join(top)
				await channel.edit(topic=topic)
				embed=discord.Embed(title=f"Well played Team 1, Team 2 your Target is {top[0]} runs")
				await ctx.send(embed=embed)
				return
			else:
				if int(top[4])<int(int(top[0])-1):
					last="GG both teams, well played! Team 1 won over Team 2 by "+str(int(top[0])-int(top[4])-1)+" runs"
					await channel.edit(topic=None)
					embed=discord.Embed(title=last)
					await ctx.send(embed=embed)
					return
				elif int(top[4])==int(int(top[0])-1):
					last="GG both teams, well played! Since it turned out to be no one's, lets go for a super-over...Team 1 will bat first"
					top[0]='0'
					top[2]='1.0'
					top[1],top[3],top[4],top[5]='0.0','0','0','0'
					top="\n".join(top)
					await channel.edit(topic=top)
					embed=discord.Embed(title=last)
					await ctx.send(embed=embed)
					return
		top[1]=temp		

	k=top
	k="\n".join(k)
	await channel.edit(topic=k)
	score=""
	if top[0]=='0':
		score+="Score: "+top[4]+"/"+top[5]+"\nOvers: "+top[1]+"/"+top[2]
	else:
		t=top[1].split(".")
		b=top[2].split(".")
		b=int(b[0])-1
		if t[1]=='0':
			t[1]=int(t[1])
		else:
			t[1]=6-int(t[1])
		t[0]=b-int(t[0])
		if t[1]==0:
			t[1]=6
		total=t[0]*6+t[1]
		score+="Score: "+top[4]+"/"+top[5]+"\nOvers: "+top[1]+"/"+top[2]+"\nNeed "+str(int(top[0])-int(top[4])) +" from "+str(total)
		if total==1:
			score+=" ball"
		else:
			score+=" balls"
	if o=='no-ball':
		last="Pull-up ur socks batsman, coz its a freehit"
	if last==None:
		embed=discord.Embed(title=f"{score}")
	else:
		embed=discord.Embed(title=f"{last}\n{score}")
	
	await ctx.send(embed=embed)
	
	
				
				
@bot.command(aliases=["so"])
async def setovers(ctx,number=None):
	topic=ctx.message.channel.topic
	if topic==None or topic=="" :
		pass
	else:
		await ctx.send("Seems like there is a match which is not done yet... Type `.end` to abandon the match")
		return
	if number==None:
		await channel.send("Syntax: `.so <number>`")
	else:
		number=int(number)
		channel=ctx.message.channel
		top="0\n0.0\n"+str(number)+".0\nNone\n0\n0"
		await channel.edit(topic=top)
		await channel.send("Overs set successfully")
@bot.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.CommandOnCooldown):
		message=await ctx.send(error)
		await asyncio.sleep(1)
		await message.delete()
bot.run(os.getenv("BOT_TOKEN"))
