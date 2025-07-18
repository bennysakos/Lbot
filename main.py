import os
import discord
from discord.ext import commands
from keep_alive import keep_alive  # Optional for 24/7 uptime on free plan

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Start web server to keep it alive (optional)
keep_alive()

# Run the bot
bot.run(os.getenv("DISCORD_TOKEN"))
