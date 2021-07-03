import os
import replit
from discord.ext import commands
from replit import db



# <----------------[MATPLOTLIB SETUP]----------------> #

os.environ['MPLCONFIGDIR'] = os.getcwd()+"/configs/"



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
  print(f"Database: {db.keys()}")

  bot.load_extension('cogs.game')
  bot.load_extension('cogs.graph')
  bot.load_extension('cogs.stack')
  bot.load_extension('cogs.postcodes')
  bot.load_extension('cogs.budget')
  
  return

bot.run(os.environ['DISCORD_BOT_TOKEN'])