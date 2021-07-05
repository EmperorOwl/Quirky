from discord.ext import commands



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



def setup(bot):
  bot.add_cog(cogOther(bot))