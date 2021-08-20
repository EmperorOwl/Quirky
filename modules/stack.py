import discord
from datetime import datetime



# <--------------[GET STACK EMBED]----------------> #

def getStackEmbed(stack, box_emoji):

  display_stack = []
  for i in range(0, 5 - len(stack)):     
    display_stack.append(box_emoji) # add white space

  display_stack += list(stack) # add coins

  embed = discord.Embed(
    title = 'Stacking Simulator',
    description =
      """
      ```To add coins use the reacts below.\nTo remove the top coin hit pop!```
      """
    ,
    timestamp = datetime.now()
  )

  embed.add_field(
    name = 'Coin Stack',
    value = "\n".join(str(i) for i in display_stack)
  )

  if len(stack) > 0:
    recent = stack[0].name
  else:
    recent = None

  total = 0
  for coin_emoji in stack:
    total += int(coin_emoji.name.replace('c', ''))

  embed.add_field(
    name = 'Summary',
    value = (
      f"Top coin: `{recent}`\n"
      f"Coin count: `{len(stack)}`\n"
      f"Total: `${'%.2f' % float(total / 100)}`"
    )
  )

  embed.set_footer(
    text = "Coins are Australian"
  )

  return embed