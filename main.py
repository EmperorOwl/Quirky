import os
import replit
import discord
from discord.ext import commands
from replit import db



# <----------------[MATPLOTLIB SETUP]----------------> #

os.environ['MPLCONFIGDIR'] = os.getcwd()+"/configs/"



# <--------------[INTENTS SETUP]------------------> #

intents = discord.Intents.default()

intents.members = True # enables bot to track number of servers and users who use the bot



# <-------------------[BOT SETUP]--------------------> #

bot = commands.Bot(

  case_insensitive = True,

  command_prefix = '.',

  intents = intents

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
  bot.load_extension('cogs.timetable')
  bot.load_extension('cogs.other')
  
  return

bot.run(os.environ['DISCORD_BOT_TOKEN'])