from discord.ext import commands



# <--------------------[COG HELP]--------------------> #

class cogHelp(commands.Cog):



  def __init__(self, bot):    
    self.bot = bot
    self.bot.remove_command('help') # removes default help command



  # <-------------------[CMD HELP]-------------------> #

  @commands.command(
    name = 'help',
    description = "View the help help!",
    aliases = ['commands', 'cmds']
  )
  async def cmdHelp(self, ctx):

    from modules.help import getHelpEmbed
    
    embed = getHelpEmbed(ctx)

    await ctx.send(embed=embed)
    
    pass



def setup(bot):
  bot.add_cog(cogHelp(bot))