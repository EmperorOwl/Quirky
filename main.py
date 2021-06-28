import os
import replit
from discord.ext import commands



# <-------------------[BOT SETUP]--------------------> #

bot = commands.Bot(

  case_insensitive = True,

  command_prefix = '.',

)



# <------------------[BOT STARTUP]-------------------> #

@bot.event
async def on_ready():

  replit.clear() # clears terminal

  print(f"Logged in as {bot.user.name} - {bot.user.id}")

  return

bot.run(os.environ['DISCORD_BOT_TOKEN'])