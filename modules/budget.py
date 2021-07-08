import discord
from replit import db



# <---------------[CALCULATE SUMMARY]----------------> #

def calcSummary(budget):

  income = int(budget['allowance']) + int(budget['job'] + int(budget['otherinc']))

  expenditure = int(budget['experiences']) + int(budget['things']) + int(budget['otherexp'])

  savings = income - expenditure

  return income, expenditure, savings



# <----------------[GET BUDGET EMBED]----------------> #

def getBudgetEmbed(ctx):

  budget = db['budgets'][str(ctx.author.id)]
  summary = calcSummary(budget)

  embed = discord.Embed(
    title = f"{ctx.author.display_name}'s Budget Calculator 💰",
    description = "```Keep track of your income, expenses and savings.```",
    color = discord.Colour.gold(),
  )

  embed.add_field(
    name = "Income",
    value = (
      f"Allowance: `${budget['allowance']:.2f}`\n"
      f"Job: `${budget['job']:.2f}`\n"
      f"Other: `${budget['otherinc']:.2f}`\n"
    )
  )

  embed.add_field(
    name = "Expenditure",
    value = (
      f"Experiences: `${budget['experiences']:.2f}`\n"
      f"Things: `${budget['things']:.2f}`\n"
      f"Other: `${budget['otherexp']:.2f}`\n"
    )
  )

  embed.add_field(
    name = "Summary",
    value = (
      f"Total Income: `${summary[0]:.2f}`\n"
      f"Total Expenditure: `${summary[1]:.2f}`\n"
      f"Total Savings: `${summary[2]:.2f}`\n"
    )
  )

  return embed