import discord 
import asyncio
import random
from discord.ext import commands
import os
bot=commands.Bot(command_prefix='.')
bot.remove_command('help')
@bot.event
async def on_ready():
	print("Less go")	
@bot.command(aliases=["t"])
async def toss(ctx):
	outcomes=["Heads","Tails"]
	answer=random.choice(outcomes)
	embed=discord.Embed(title='Toss')
	embed.set_image(url="https://tenor.com/view/quarter-coin-flip-heads-tails-gif-14158378")
	message=await ctx.send(embed=embed)
	await asyncio.sleep(4)	
	embed=discord.Embed(title=f'Oh! Its a {answer}')
	await message.edit(embed=embed)
@bot.command(aliases=["b"])
async def bowl(ctx):
	outcomes=[2, 1, 1, 1, 1, 2, 3, 0, 4, 2, 1, 1, 1, 4, 2, 6,  'no-ball',3, 3, 1, 2, 1, 0, 3, 1, 1, 4, 6, 4, 2, 1, 'wicket', 3, 0, 0, 3, 6, 6, 1, 'wicket', 'wide', 1, 3, 3, 3, 0, 3, 'wicket', 3, 4, 2, 2, 6, 3, 0, 'wicket', 'wide', 3, 1, 3, 6, 6, 4,2, 1, 3, 3, 3, 'wide', 'wide', 2, 6, 0, 2, 2, 3, 4, 2, 4, 3, 4, 2, 2, 4, 6, 3, 'no-ball', 0, 2, 1, 2, 1, 2, 1, 'wicket', 'wicket', 'no-ball', 2, 0, 2, 0, 6, 'wide', 'wicket', 1]
	o=random.choice(outcomes)
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
		txt="Bull's eye! The bowler doesn't miss the stumps this time"
	embed=discord.Embed(title=txt)
	embed.set_image(url=f'{img}')
	await ctx.send(embed=embed)	
	
bot.run(os.getenv("BOT_TOKEN"))
