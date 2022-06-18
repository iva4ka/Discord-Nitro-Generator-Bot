import discord
import requests
import json
import datetime, time
from discord.ext import commands

client = discord.Client()

client = commands.Bot(command_prefix = '!')

@client.command()
async def randompasswordgenerator(ctx, *, length: str = '16') -> None:
  length = int(length)
  string = lower + upper + numbers + symbols
  password = "".join(random.sample(string, length))
  embed = discord.Embed(title="Here is your randomly generated password.", description=f"**{password}**")
  await ctx.send(embed=embed)

client.run("TOKEN HERE")
