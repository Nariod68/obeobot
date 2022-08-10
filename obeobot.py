from datetime import datetime
from email import message
from enum import Enum
from http import client
from math import floor
from textwrap import indent
from turtle import color, title
from unicodedata import name
from unittest import result
import discord
from discord.ext import commands, tasks
import youtube_dl
import asyncio
import time
from random import randint
import asyncio
import functools
import itertools
import math
import random
import discord
import youtube_dl
from async_timeout import timeout
from discord.ext import commands
from itertools import cycle
import datetime
import asyncio
from discord.ext.commands import bot
import re
import time
from youtube_dl import YoutubeDL
import youtube_dl
import asyncio

TOKEN = "token ici"

bot = commands.Bot(command_prefix="!", description="Mon créateur est nariod ")

musics = { }
ytdl = youtube_dl.YoutubeDL()

@bot.event
async def on_ready():
    print("I'm alive")
    await bot.change_presence(activity=discord.Game(name="!Help"), status = discord.Status.online)
    



@bot.command()
async def exemple(ctx):
    await ctx.message.delete()
    await ctx.send("Ceci est un message exemple")

@bot.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, user:discord.User, *, reason ="Aucune raison fournie"):
    await ctx.message.delete()
    embed = discord.Embed(Title="Warn", description="Un modérateur a averti un membre", color = discord.Color.orange())
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVypp2i00dUIHySLwNd9-ckGlzTQhjPTc9cA&usqp=CAU")
    embed.add_field(name="Membre averti:", value=user.name+"#"+str(user.discriminator))
    embed.add_field(name="Invoker:", value=ctx.author.name+"#"+str(ctx.author.discriminator), inline=True)
    embed.add_field(name="Raison", value=reason, inline=False)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user : discord.User, *, reason=None):
    await ctx.message.delete()
    if reason is None:
        embed=discord.embed(title=":warning: Erreur dans la commande de ban", description="Largument `reason` est requis", color = discord.Color.blurple())
        await ctx.send(embed=embed)
    else:
            await ctx.guild.ban(user, reason=reason)
            embed=discord.embed(title="Un membre a été banni", description="Un modérateur/administrateur a banni un utilisateur", color=discord.Color.dark_red())
            embed.add_field(name="Membre banni", value=user.name+"#"+str(user.discriminator))
            embed.add_field(name="Invoker:", value=ctx.author.name+"#"+str(ctx.author.discriminator), inline=True)
            embed.add_field(name="Raison", value=reason, inline=False)
            await ctx.send(embed=embed)

@bot.command()
async def coucou(ctx):
    await ctx.message.delete()
    await ctx.send("Coucou !")

@bot.command()
async def serverInfo(ctx):
    await ctx.message.delete()
    server = ctx.guild
    number0fTextchannels = len(server.text_channels)
    number0fVoicechannels = len(server.voice_channels)
    serverDescription = server.description
    number0fPerson = server.member_count
    servername = server.name
    message = f"Le serveur *{servername}* contient {number0fPerson} personnes. \nLa description du serveur {serverDescription}. \nCe serveur possède {number0fTextchannels} salons écrit(s) ainsi que {number0fVoicechannels} salons vocaux."
    await ctx.send(message)

@bot.command()
async def say(ctx, *texte):
    await ctx.message.delete()
    await ctx.send(" ".join(texte))


@bot.command()
async def kick(ctx, user : discord.User, *reason):
    await ctx.message.delete()
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason = reason)
    await ctx.send(f"{user} à bien été kick du serveur.")

@bot.command()
async def clear(ctx, nombre : int):
    await ctx.message.delete()
    messages = await ctx.channel.history(limit = nombre + 1).flatten()
    for message in messages:
        await message.delete()

@bot.command()
async def unban(ctx, user, *reason):
    await ctx.message.delete()
    userName, userID = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userID:
            await ctx.guild.unban(i.user, reason = reason)
            em = discord.embed(description = f"{user} a été **unban** par {ctx.author}!", color = 0x000000)
            await ctx.send(embed = em)
            return

    await ctx.send(f"{user} ne figure pas dans la liste des utilisateurs bannis.")

@bot.command()
async def Help(ctx):
    embed=discord.Embed(title = 'Help',description = 'help for you',color = discord.Color.green())
    embed.set_footer(text=f'Requested by - {ctx.author}',icon_url=ctx.author.avatar_url)
    embed.add_field(name='General',value='`(Pas encore évoqué)`')
    embed.add_field(name='Moderation',value='`DM`, `say`, `kick`, `ban`, `unban`, `warn` , `clear`, `nick`',inline=False)
    embed.add_field(name='Fun/Tests',value='`exemple`, `coucou`, `dé,dés ou dices`', inline=False)
    embed.add_field(name='Music',value='`play (url)`, `pause`, `resume`, `leave`, `skip`' , inline=False)
    embed.add_field(name='Prefix', value='`!`', inline=False)
    await ctx.send (embed=embed)

@bot.command()
async def DM(ctx, user: discord.User,*, message=None):
    message = message or "Test"
    await user.send(message)
    await ctx.message.delete()

@bot.command(pass_content=True)
async def nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention}')


@bot.command()
async def prefix(ctx):
    embed = discord.Embed(
        title = 'Le préfixe du bot est : !',
        color = discord.Color.random()
    )
    await ctx.send (embed=embed)





@bot.command(pass_context=True, name="dice", aliases = ["dé", "dés", "dices"])
async def dice(ctx,nb:int) :
    result = randint(1,nb)
    embed=discord.Embed(
        title = f"Tirage d'un dé de {nb} faces",
        description = f"Le dé tombe sur `{result}`! 🎲",
        color = 0xAE02A1
    )
    embed.set_author(name = ctx.message.author.name, url = "https://crdev.xyz/" ,icon_url = ctx.message.author.avatar_url)
    await ctx.send(embed=embed)


class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]


@bot.command()
async def leave(ctx):
    client = ctx.guild.voice_client
    await client.disconnect()
    musics[ctx.guild] = []

@bot.command()
async def resume(ctx):
    client = ctx.guild.voice_client
    if client.is_paused():
        client.resume()


@bot.command()
async def pause(ctx):
    client = ctx.guild.voice_client
    if not client.is_paused():
        client.pause()



@bot.command()
async def skip(ctx):
    client = ctx.guild.voice_client
    client.stop()


def play_song(client, queue, song):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url
        , before_options= "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))
    
    def next(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            play_song(client, queue, new_song)
        else:
            asyncio.run_coroutine_threadsafe(client.disconnect(), bot.loop)

    client.play(source, after=next)


@bot.command()
async def play(ctx, url):
    print("play")
    client = ctx.guild.voice_client

    if client and client.channel:
        video = Video(url)
        musics[ctx.guild].append(video)
    else:
        channel = ctx.author.voice.channel
        video = Video(url)
        musics[ctx.guild] = []
        client = await channel.connect()
        await ctx.send(f"Je lance : {video.url}")
        play_song(client, musics[ctx.guild], video)







bot.run(TOKEN)
