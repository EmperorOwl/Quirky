from discord.ext import commands
from replit import db


from modules.budget import getBudgetEmbed


# <-----------------[COG BUDGET]------------------> #

class cogBudget(commands.Cog, name="Budget Calculator"):

  

  def __init__(self, bot):
    self.bot = bot

  

  # <----------------[GRP BUDGET]-----------------> #

  @commands.group(
    name = 'budget',
    description = "Calculate your savings!",
    aliases = ['bdg']
  )
  async def grpBudget(self, ctx):

    if str(ctx.author.id) not in db['budgets'].keys():

      db['budgets'].update({
        ctx.author.id: {
          'allowance': 0,
          'job': 0,
          'otherinc': 0,
          'experiences': 0,
          'things': 0,
          'otherexp':0,
        }
      })

    if ctx.invoked_subcommand is None:

      content = f"**💰  |  {ctx.author.name}**, incorrect subcommand passed!\n*Use either `budget view`, `budget add` or `budget reset`.*"

      await ctx.send(content=content)

    return



  # <-----------------[CMD VIEW]------------------> #

  @grpBudget.command(name='view')
  async def cmdView(self, ctx):

    embed = getBudgetEmbed(ctx)

    await ctx.send(embed=embed)

    return



  # <-----------------[CMD ADD]-------------------> #

  @grpBudget.command(name='add')
  async def cmdAdd(self, ctx, form, amount: float):

    budget = db['budgets'][str(ctx.author.id)]

    if form in budget.keys():

      budget.update({form: amount})

      content = f"**💹 | {ctx.author.display_name}**, successfully added `${amount:.2f}` to `{form.title()}`."

    else:

      content = f"**☹️ | {ctx.author.display_name}**, incorrect type of budget.\nUse either `allowance`, `job`, `otherinc`, `experiences`, `things` or `otherexp`."

    await ctx.send(content=content)

    return



  # <----------------[CMD RESET]------------------> #

  @grpBudget.command(name='reset')
  async def cmdReset(self, ctx):

    del db['budgets'][str(ctx.author.id)]

    content = f"**😥 | {ctx.author.display_name}**, your budget has been reset."

    await ctx.send(content=content)

    return

  

  # <----------------[CMD SETUP]------------------> #

  @commands.command(
    name = 'budgetsetup',
    description = "Setup or reset budget database."
  )
  @commands.is_owner()
  async def cmdSetup(self, ctx):
    
    db['budgets'] = {}

    content = f"**💰  |  {ctx.author.name}**, budget database has undergone first setup or full reset."

    await ctx.send(content=content)

    return



def setup(bot):
  bot.add_cog(cogBudget(bot))