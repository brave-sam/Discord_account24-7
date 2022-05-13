#THIS CODE HELP YOU TO HOST YOUR DISCORD ACCOUNT 24/7

import discord
import os
import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix=':', self_bot=True, help_command=None)

async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game("TESTING"))

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)


"""
THIS CODE IS WRITTEN IN PYTHON AND CODE IS WRITTEN BY Sam 🦋#5606
"""
