import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents, self_bot=True, help_command=None)
client.remove_command("help")
token = 'NzQyMDEyODc0MDMyOTM5MDE5.JY9S3Oi.zOzK7lVGTjU34QHD7PLwKxepcYD'
@client.event
async def on_ready():
  print(f"Logged in as {client.user.name} #{client.user.discriminator}")

@client.command()
async def s(ctx, m):
  await ctx.send(m)

client.run(token, bot=False)
