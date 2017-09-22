import discord
from discord.ext import commands
import random

rockpapersi = {
    'rock' : 'scissors',
    'scissors' : 'paper',
    'paper' : 'rock'
}
eigball = [
    'count on it',
    "Don't count on it", 
    'Yes absolutely',
    'No are you stupid',
    'The answer is yes',
    'The answer is no'
]
description = '''There are a number of utility commands being showcased here.
   
'''
bot = commands.Bot(command_prefix='ayy ', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(description="Use the command ayy rps {Rock paper or scisssors} to verse the bot 1 on 1")
async def rps(res : str):
    '''Use the command ayy rps {Rock paper or scisssors}'''
    choice = ['rock', 'paper', 'scissors']
    randchoi = random.choice(choice)
    print(randchoi)
    compres = rockpapersi[randchoi]
    print(compres)
    if res == compres:
        await bot.say("```I chose {} \n You Lose```".format(randchoi))
    elif res == randchoi: 
        await bot.say("```I chose {} \n Tie```".format(randchoi))
    elif res != compres:
        await bot.say("```I chose {} \n :trophy:You Win```".format(randchoi))
@bot.command(description="Use the command ayy eightball {question} to see what your future will bring")
async def eightball(*message: str):
    '''Use the command ayy eightball {question}'''
    for mes in message:
        if "" in mes:
            await bot.say(
                ':8ball: Please actually type something you brain dead shit'
                )
    randomans = random.choice(eigball)
    await bot.say(':8ball: {}'.format(randomans))
@bot.command(description="Use the command ayy roll {number} to choose a number between 1 - that number")
async def roll():
    '''Use the command ayy roll'''
    dices = [1, 2, 3, 4, 5, 6]
    rroll = random.choice(dices)
    await bot.say(rroll)

@bot.command()
async def flip():
    ht = ["Heads", "Tails"]
    rht = random.choice(ht)
    await bot.say(":game_die: {}".format(rht))
@bot.command()
async def info(user: discord.Member):
    await bot.say("``` Roles: {} \n First joined server at: {} \n Status: {} \n Currently Playing: {} \n Nickname: {} \n```".format(
        user.top_role, user.joined_at, user.status, user.game, user.nick))

bot.run('MzYwMTk2OTcwNjk2MDE1ODcy.DKSEqA.9CbvdVeCg_rIfaZhBJmUJcydUCo')