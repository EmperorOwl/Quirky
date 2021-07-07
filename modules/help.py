import discord
from datetime import datetime



# <-----------------[GET HELP EMBED]-----------------> #

def getHelpEmbed(ctx):

  from storage import bot_version

  embed = discord.Embed(
    title = 'Help Page',
    description = f"Prefix: `{ctx.prefix}`",
    color = discord.Colour.purple(),
    timestamp = datetime.now()
  )

  cogs = list(ctx.bot.cogs.values())[:-3] # remove other, eror and help cogs

  for cog in cogs:
    
    cmd_name = cog.get_commands()[0].name
    cmd_info = cog.get_commands()[0].description

    embed.add_field(
      name = cog.qualified_name,
      value = f"`{ctx.prefix}{cmd_name}` - {cmd_info}",
      inline = False
    )

  cog_other = ctx.bot.get_cog('cogOther')
  other_cmds = list(cog_other.get_commands())[:-1] # remove owner only command
  
  embed.add_field(
    name = 'Other',
    value = " ".join(f'`{c.name}`' for c in other_cmds)
  )

  embed.set_footer(text=f'Version {bot_version}')

  return embed