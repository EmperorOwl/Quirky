import discord
import psutil
import sys



# <----------------[GET ABOUT EMBED]-----------------> #

def getAboutEmbed(ctx):

  from storage import bot_version

  per = psutil.virtual_memory().percent
  used = round(per / 100 * 4, 2)
  percent = round(used / 4 * 100, 2)
  memory = f'{used} GB used out of 4.00 GB ({percent}%)'
  latency = round(ctx.bot.latency*1000, 2)

  embed = discord.Embed(
    title = 'About Me',
    description = (

      "Hey everyone! My name is EmperorOwl and I have created Quirky, a funky Discord bot with wacky features. Hope you enjoy!\n"

      '\n'

      f"`      Developer:` EmperorOwl#4400\n"
      f"`        Servers:` {len(ctx.bot.guilds)}\n"
      f"`          Users:` {len(ctx.bot.users)}\n"
      f"`       Commands:` {len(ctx.bot.commands)}\n"
      f"`         Memory:` {memory}\n"
      f"`      CPU Usage:` {psutil.cpu_percent()}%\n"
      f"`        Latency:` {latency} ms\n"
      f"`    Bot Version:` {bot_version}\n"
      f"` Python Version:` {sys.version[:6]}\n"
      f"`       Platform:` Replit — Hacker (Always On + Boosted)\n"

      '\n'

      "[Replit Spotlight](https://replit.com/@EmperorOwl/Quirky) ~ [Top.gg Site](https://top.gg/bot/848030918920634448) ~ [Invite Me](https://discord.com/api/oauth2/authorize?client_id=848030918920634448&permissions=1074063424&scope=bot) ~ [Github Repository](https://github.com/EmperorOwl/Quirky)"

    ),
    color = discord.Colour.purple()
  )

  return embed