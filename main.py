import os
import discord
from discord.ext import commands
from keep_alive import keep_alive  # Optional for 24/7 uptime on free Render

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.listening, name="got hacked")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Optional: Start Flask server to keep alive
keep_alive()

# Run the bot using the environment token
bot.run(os.getenv("DISCORD_TOKEN"))

