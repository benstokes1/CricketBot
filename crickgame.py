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
	embed.set_image(url=f"{}")
	message=await ctx.send(embed=embed)
	await asyncio.sleep(3)	
	embed=discord.Embed(title=f'Oh its a {answer}')
	await message.edit(embed=embed)
@bot.command(aliases=["b"])
async def bowl(ctx):
	outcomes=[2, 'no-ball', 1, 1, 1, 1, 2, 3, 0, 4, 2, 1, 1, 1, 4, 2, 6, 3, 3, 1, 2, 1, 0, 3, 1, 1, 4, 6, 4, 2, 1, 'wicket', 'no-ball', 3, 0, 0, 3, 6, 6, 'wicket', 1, 'wicket', 'wicket', 'wicket', 'wide', 1, 3, 3, 3, 0, 3, 'wicket', 3, 4, 2, 2, 6, 3, 0, 'wicket', 'wide', 3, 1, 3, 6, 6, 4, 'no-ball', 2, 1, 3, 3, 3, 'wide', 'wide', 2, 6, 0, 2, 2, 3, 4, 2, 4, 3, 4, 2, 2, 4, 6, 3, 'no-ball', 0, 2, 1, 2, 1, 2, 1, 'wicket', 'wicket', 'no-ball', 2, 0, 2, 0, 6, 'wide', 'wicket', 1]
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
		img='https://tenor.com/view/kstr-kochstrasse-four-gif-14628115'
		txt='Smashed into the gap for a FOUR'
	if o==6:
		img='https://tenor.com/view/six-six-six-going-up-pointing-up-andre-russell-kkr-hai-taiyaar-gif-13941061'
		txt="The fielder can do nothing but watch the ball sail over his head, its a SIX!"
	if o=='no-ball':
		img='https://tenor.com/view/no-ball-cricket-umpire-man-standing-gif-17020197'
		txt="The bowler stepped this time, it's a no ball"
	if o=='wide':
		img='https://tenor.com/view/wide-wide-ball-cricket-funny-cricket-bowler-gif-16733235'
		txt="Extra runs for the batting team, it's a wide"
	if o=='wicket':
		img='https://tenor.com/view/its-awicket-happy-jumping-cheering-satisfied-gif-13800701'
		txt=["Bull's eye! The bowler doesn't miss the stumps this time","The fielder pulled out a blinder, very good catch!"]
		txt=random.choice(txt)
	embed=discord.Embed(title=txt)
	embed.set_img(url=f'{img}')
	await ctx.send(embed=embed)	      
bot.run(os.getenv("BOT_TOKEN"))
