import discord
import requests
import json
import datetime, time
from discord.ext import commands

client = discord.Client()

client = commands.Bot(command_prefix = '!')

@client.command()
async def nitrogen(ctx):
  code = "https://discord.gift/" + ('').join(
	random.choices(string.ascii_letters + string.digits, k=16))
  embed = discord.Embed(title="Here is the generated nitro link!", description=f"{code}")
  embed.set_thumbnail(url='https://i.ibb.co/hf4yqpp/Nitro-badge.png')
  embed.set_footer(text="Source Code: https://github.com/Ocryol1337/Discord-Nitro-Generator-Bot")
  await ctx.send(embed=embed)

client.run("TOKEN HERE")
