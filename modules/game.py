import discord
import random
import os
from datetime import datetime


from storage import reactions_dict


# <-----------------[GET GAME INFO]------------------> #

def getGameInfo():

  images = os.listdir("images")
  random_image = random.choice(images)
  fp = f"images/{random_image}"

  word = random_image[4:].replace('.png', '')
  letter = random_image[1]
  emoji_answer = reactions_dict[letter]

  reactions = list(reactions_dict.values())
  reactions.remove(reactions_dict[letter])
  reactions = random.sample(reactions, 4)
  reactions.append(reactions_dict[letter])
  reactions = sorted(reactions)

  game_info = {
    'fp': fp,
    'word': word,
    'reactions': reactions,
    'emoji_answer': emoji_answer,
  }

  return game_info



# <-----------------[GET GAME EMBED]-----------------> #

def getGameEmbed(description, colour):

  embed = discord.Embed(
    title = "Match the Alphabet",
    description = description,
    colour = colour,
    timestamp = datetime.now(),
  )

  embed.set_image(url='attachment://image.png')
  embed.set_footer(text="Image from Clipart Library")

  return embed