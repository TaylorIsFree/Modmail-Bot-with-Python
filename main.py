from discord.ext import commands
import discord
import os

intents = discord.Intents.default()
# we need members intent too
intents.members = True

bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.event
async def on_ready():
	print("The bot is online!")
	bot.load_extension("cogs.onMessage")

bot.run(os.environ.get("Nzc5Njg2ODg1NDYzMDMxODE4.X7kJ_w.8jmyiftKYPCX0EhrAYqzp-CP3bc"))
