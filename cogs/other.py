import time
import discord
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


  # <-------------------[CMD PING]-------------------> #

  @commands.command(
    name = 'ping',
    description = "Check the ping.",
    aliases = []
  )
  async def cmdPing(self, ctx):

    start = time.perf_counter()
    msg = await ctx.send(content="Pinging...")
    end = time.perf_counter()
    t_t = (end - start) * 1000
    await msg.edit(content="Pong! {:.2f}ms".format(t_t))

    return



  # <------------------[CMD INVITE]------------------> #

  @commands.command(
    name = 'invite',
    description = "Add Quirky to another server.",
    aliases = []
  )
  async def cmdInvite(self, ctx):

    embed = discord.Embed(
      title = "Thanks for playing with Quirky!",
      description = "To add the bot to another server, click [here](https://discord.com/api/oauth2/authorize?client_id=848030918920634448&permissions=1074063424&scope=bot).",
      color = discord.Colour.blue()
    )

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