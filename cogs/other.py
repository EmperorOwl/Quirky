from discord.ext import commands
from replit import db



# <-------------------[COG OTHER]--------------------> #

class cogOther(commands.Cog):



  def __init__(self, bot):
    self.bot = bot



  # <------------------[CMD ABOUT]-------------------> #

  @commands.command(
    name = 'about',
    description = "Check out some stats!"
  )
  async def cmdAbout(self, ctx):

    from modules.other import getAboutEmbed

    embed = getAboutEmbed(self)

    await ctx.send(embed=embed)
  
    return



  # <------------------[CMD PREFIX]------------------> #

  @commands.command(
    name = 'prefix',
    description = "Change the prefix.",
    aliases = []
  )
  async def cmdPrefix(self, ctx, prefix):

    db['prefixes'] = {
      ctx.guild.id: {'prefix': prefix}
    }

    content = f"**👍 | {ctx.author.display_name}**, the prefix to play with Quirky in this server has been changed to `{prefix}`"

    await ctx.send(content=content)

    return

  

  # <------------------[CMD SETUP]-------------------> #

  @commands.command(
    name = 'prefixsetup',
    description = "Setup or reset prefix database."
  )
  @commands.is_owner()
  async def cmdSetup(self, ctx):
    
    db['prefixes'] = {}

    content = f"**👍  |  {ctx.author.name}**, prefix database has undergone first setup or full reset."

    await ctx.send(content=content)

    return



def setup(bot):
  bot.add_cog(cogOther(bot))