from discord.ext import commands
from replit import db


from modules.timetable import getTimetableEmbed


# <-----------------[COG TIMETABLE]------------------> #

class cogTimetable(commands.Cog, name="Timetable Manager"):



  def __init__(self, bot):
    self.bot = bot

  

  # <----------------[GRP TIMETABLE]-----------------> #

  @commands.group(
    name = 'timetable',
    description = "View and edit a school timetable!",
    aliases = []
  )
  async def grpTimetable(self, ctx):

    if str(ctx.author.id) not in db['timetables'].keys(): 
 
      db['timetables'].update({
        ctx.author.id: {
          'monday': 
            ['P1', 'P2', 'P3', 'P4', 'P5', 'P6'],
          'tuesday': 
            ['P1', 'P2', 'P3', 'P4', 'P5', 'P6'],
          'wednesday': 
            ['P1', 'P2', 'P3', 'P4', 'P5', 'P6'],
          'thursday': 
            ['P1', 'P2', 'P3', 'P4', 'P5', 'P6'],
          'friday': 
            ['P1', 'P2', 'P3', 'P4', 'P5', 'P6'],
        }
      })
    
    if ctx.invoked_subcommand is None:

      content = f"**✉️  |  {ctx.author.name}**, incorrect subcommand passed!\n*Use either `timetable view` or `timetable edit`.*"

      await ctx.send(content=content)

    return


  
  # <-------------------[CMD VIEW]-------------------> #

  @grpTimetable.command(name='view')
  async def cmdView(self, ctx):

    embed = getTimetableEmbed(ctx)

    await ctx.send(embed=embed)

    return



  # <-------------------[CMD EDIT]-------------------> #
  
  @grpTimetable.command(name='edit')
  async def cmdEdit(self, ctx, day, p1, p2, p3, p4, p5, p6):

    day = day.lower()
    timetable = db['timetables'][str(ctx.author.id)]

    if day in timetable.keys():

      timetable.update({day: [p1, p2, p3, p4, p5, p6]})

      content = f"**📅 | {ctx.author.display_name}**, successfully updated your schedule for {day.title()}."

    else: 

      content = f"**☹️ | {ctx.author.display_name}**, that is not a weekday. Use either Monday, Tuesday, Wednesday, Thursday or Friday."

    await ctx.send(content=content)

    return



  # <------------------[CMD RESET]-------------------> #

  @grpTimetable.command(name='reset')
  async def cmdReset(self, ctx):

    del db['timetables'][str(ctx.author.id)]

    content = f"**😥 | {ctx.author.display_name}**, your timetable has been reset."

    await ctx.send(content=content)

    return



  # <------------------[CMD SETUP]-------------------> #

  @commands.command(
    name = 'timetablesetup',
    description = "Setup or reset timetable database."
  )
  @commands.is_owner()
  async def cmdSetup(self, ctx):
    
    db['timetables'] = {}

    content = f"**📅  |  {ctx.author.name}**, timetable database has undergone first setup or full reset."

    await ctx.send(content=content)

    return



def setup(bot):
  bot.add_cog(cogTimetable(bot))