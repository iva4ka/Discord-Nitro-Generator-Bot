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
  embed.set_thumbnail(url='')
  embed.set_footer(text="iva4ka")
  await ctx.send(embed=embed)

@client.command()
async def nitrogen(ctx):
  code = "https://discord.gift/" + ('').join(
	random.choices(string.ascii_letters + string.digits, k=16))
  await ctx.send(f"{code}")


client.run("TOKEN HERE")
