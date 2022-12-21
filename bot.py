import discord
from discord.ext import commands


import praw
from praw.reddit import Subreddit
import random

reddit=praw.Reddit( client_id="t4TgY-mFW3b7g7qyGunOEA",
                    client_secret="o6gByXt1hYTcd9pv8puAjBuACUwMEA",
                    username="pythonproject420",
                    password="pythonproject@420",
                    user_agent="pythonpraw")

from image_cog import image_cog

from music_cog import music_cog


Bot=commands.Bot(command_prefix='/')




Bot.add_cog(image_cog(Bot))

Bot.add_cog(music_cog(Bot))




#activity status when online 
@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Game(name='KEEPING IT REAL')) 



@Bot.command()
async def hi(ctx):
    await ctx.send("hi my name is Mike, Mike Oxmoll")




#meme from reddit and subreddit 
@Bot.command()
async def meme(ctx,subred="memes"):
        subreddit= reddit.subreddit(subred)
        
        subs=[]

        top=subreddit.top(limit=15)

        for i in top:
            subs.append(i)
        
        random_sub=random.choice(subs)

        name=random_sub.title
        url=random_sub.url
        em=discord.Embed(tittle=name)
        em.set_image(url=url)
        await ctx.send(embed=em)
        



token=""
with open("token.txt") as file:
    token=file.read()
Bot.run(token)