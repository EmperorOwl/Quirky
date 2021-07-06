import sys
import traceback
from discord.ext import commands



# <-------------------[COG ERROR]--------------------> #

class cogError(commands.Cog):



  def __init__(self, bot):
    self.bot = bot

  

  # <----------------[LISTENER ERROR]----------------> #

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):

    """
    The event triggered when an error is raised while invoking a command.

    Parameters
    ----------
    ctx: commands.Context
      The context used for command invocation
    error: commands.CommandError
      The Exception raised
      
    """

    # <----------[ERROR COMMAND NOT FOUND]-----------> #

    if isinstance(error, commands.CommandNotFound):

      pass



    # <-----------[ERROR COMMAND DISABLED]-----------> #

    elif isinstance(error, commands.DisabledCommand):

      content = f"**🔒 | {ctx.author.display_name}**, that command is currently disabled."

      await ctx.send(content=content)



    # <-----------[ERROR ARGUMENT MISSING]-----------> #

    elif isinstance(error, commands.MissingRequiredArgument):

      if ctx.command.qualified_name == 'graph':
        
        content = f"**☹️ | {ctx.author.display_name}**, you are missing one or a combination of an equation, lower bound and upper bound for x. The syntax is `.graph <equation> <lower> <upper>`"
        
      elif ctx.command.qualified_name == 'postcodes find':

        content = f"**☹️ | {ctx.author.display_name}**, your are missing the suburb or the postcode to find.\nThe syntax is `.postcodes find <suburb/postcode>`"

      elif ctx.command.qualified_name == 'postcodes add':

        content = f"**☹️ | {ctx.author.display_name}**, your are missing the suburb and the postcode to add.\nThe syntax is `.postcodes add <suburb> <postcode>`"

      elif ctx.command.qualified_name == 'postcodes delete':

        content = f"**☹️ | {ctx.author.display_name}**, your are missing the suburb to delete.\nThe syntax is `.postcodes delete <suburb>`"

      elif ctx.command.qualified_name == 'budget add':

        content = f"**☹️ | {ctx.author.display_name}**, you are missing what type of budget and/or what amount to add.\nThe syntax is `.budget add <type> <amount>`"

      elif ctx.command.qualified_name == 'timetable edit':

        content = f"**☹️ | {ctx.author.display_name}**, you are missing the day and/or six periods to edit.\nThe syntax is `.timetable edit <day> <P1> <P2> <P3> <P4> <P5> <P6>`"

      elif ctx.command.qualified_name == 'prefix':

        content = f"**☹️ | {ctx.author.display_name}**, you are missing what to change the prefix to."

      await ctx.send(content=content)
        


    # <-------------[ERROR ARGUMENT BAD]-------------> #

    elif isinstance(error, commands.BadArgument):

      if ctx.command.qualified_name == 'graph':

        content = f"**☹️ | {ctx.author.display_name}**, the lower and upper bounds for x have to be numbers."

      elif ctx.command.qualified_name == 'budget add':

        content = f"**☹️ | {ctx.author.display_name}**,the amount to add must be a number!\nThe correct syntax is `.budget add <type> <amount>`." 

      await ctx.send(content=content)
      
    else:
      
      print("Ignoring exception in command {}:".format(ctx.command), file=sys.stderr)
      traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    return



def setup(bot):
  bot.add_cog(cogError(bot))