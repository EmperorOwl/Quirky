import os
import replit
import topgg
import discord
from discord.ext import commands
from replit import db



# <--------------[MATPLOTLIB SETUP]---------------> #

os.environ['MPLCONFIGDIR'] = os.getcwd()+"/configs/"



# <---------------[INTENTS SETUP]-----------------> #

intents = discord.Intents.default()

intents.members = True # enables bot to track number of servers and users who use the bot



# <----------------[PREFIX SETUP]-----------------> #

def get_prefix(client, message):

  try: # search for custom prefix

    prefix = db['prefixes'][str(message.guild.id)]['prefix']

  except KeyError: # otherwise set default one

    prefix = 'q!'

  return prefix



# <-----------------[BOT SETUP]-------------------> #

bot = commands.Bot(

  case_insensitive = True,

  command_prefix = get_prefix,

  intents = intents

)



# <----------------[TOPGG SETUP]------------------> #

bot.topggpy = topgg.DBLClient(
  bot, 
  token = os.environ['TOP_GG_TOKEN'], 
  autopost = True, 
  post_shard_count= True
)



# <----------------[TOPGG UPDATE]-----------------> #

@bot.event
async def on_autopost_success():
  
  # updates top.gg server count every half hour
  print(f"Posted server count ({bot.topggpy.guild_count}) to top.gg")

  return



# <----------------[BOT STARTUP]------------------> #

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
  bot.load_extension('cogs.error')
  bot.load_extension('cogs.help')
  
  return

bot.run(os.environ['DISCORD_BOT_TOKEN'])