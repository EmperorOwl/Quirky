import discord
import pytz
from replit import db
from datetime import datetime



# <--------------[GET TIMETABLE EMBED]---------------> #

def getTimetableEmbed(ctx):

  timetable = db['timetables'][str(ctx.author.id)]

  aus = pytz.timezone("Australia/Melbourne")

  embed = discord.Embed(
    title = f"{ctx.author.display_name}'s Timetable Manager 📅",
    description = f'```ini\nKeep track of your classes. Current time: [{datetime.now().astimezone(aus).strftime("%H:%M:%S")}]```',
    color = discord.Colour.green()
  )

  for day in timetable:

    schedule = [d for d in timetable[day]]
    schedule.insert(2, '; Recess ;')
    schedule.insert(5, '; Lunch ;')

    embed.add_field(
      name = day.title(),
      value = "```ini\n" + "\n".join(s for s in schedule) + "```"
    )

  return embed