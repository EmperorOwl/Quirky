import discord
from discord.ext import commands
from datetime import datetime



# <-------------------[COG GRAPH]--------------------> #

class cogGraph(commands.Cog, name="Graphing Calculator"):



  def __init__(self, bot):    
    self.bot = bot



  # <------------------[CMD GRAPH]-------------------> #

  @commands.command(
    name = 'graph',
    description = "Plot the graph of an equation!",
  )
  async def cmdGraph(self, ctx, equation, lower: float, upper: float):

    from modules.graph import plotGraph

    start_time = datetime.now()
    plotGraph(equation, lower, upper)
    end_time = datetime.now()

    t_t = (end_time - start_time).total_seconds()

    embed = discord.Embed(
      title = f"{ctx.author.display_name}'s Graph",
      description = (
        f"Equation: `{equation}, x∈{lower, upper}`\n"
        "Syntax: `.graph <eq> <lower> <upper>`\n"
        f"Time taken: `{t_t} s`"
      ),
      color = discord.Color.blue(),
      timestamp = datetime.now(),
    )

    file = discord.File("graph.png")
    embed.set_image(url="attachment://graph.png")
    embed.set_footer(text='Powered by Matplotlib')

    await ctx.send(file=file, embed=embed)

    return



def setup(bot):
  bot.add_cog(cogGraph(bot))