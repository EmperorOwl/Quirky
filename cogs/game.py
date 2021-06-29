import discord
import asyncio
from discord.ext import commands



# <--------------------[COG GAME]--------------------> #

class cogGame(commands.Cog, name="Children's Toy"):



  def __init__(self, bot):    
    self.bot = bot


    

  # <-------------------[CMD PLAY]-------------------> #

  @commands.command(
    name = "play",
    description = "Play the alphabet game!",
  )
  async def cmdPlay(self, ctx):

    from modules.game import getGameInfo
    from modules.game import getGameEmbed

    game_info = getGameInfo()

    file = discord.File(
      fp = game_info['fp'],
      filename = 'image.png'
    )

    embed = getGameEmbed(
      description = 'Click the letter I begin with!',
      colour = discord.Colour.blue(),
    )

    msg = await ctx.send(file=file, embed=embed)

    for reaction in game_info['reactions']:
      await msg.add_reaction(reaction)

    switch = 1
    while True:

      def check(reaction, user):
        return reaction.message.id == msg.id and user.name != self.bot.user.name

      try: 

        reaction, user = await self.bot.wait_for(
          'reaction_add',
          timeout = 120, 
          check = check
        )

        emoji = str(reaction)
        await msg.remove_reaction(reaction, user)

        # user reacts on correct letter
        if emoji == game_info['emoji_answer']:
          
          embed = getGameEmbed(
            description = f"Congratulations {user.mention}!\nYou got the answer: {game_info['emoji_answer']} for `{game_info['word']}`!",
            colour = discord.Colour.green()
          )

          await msg.edit(embed=embed)
          await msg.clear_reactions()

          break

        # user reacts on incorrect letter
        else:

          if switch == 1: 

            embed = getGameEmbed(
              description = "Oops! Try again!",
              colour = discord.Colour.red(),
            )

            switch = 2

          elif switch == 2:

            embed = getGameEmbed(
              description = "Oh no! That’s wrong!",
              colour = discord.Colour.orange()
            )

            switch = 1

          await msg.edit(embed=embed)
      
      except asyncio.TimeoutError:

        embed = getGameEmbed(
          description = "Time's up! To play again, type `.play`!",
          colour = discord.Colour.light_grey(),
        )
        
        await msg.edit(embed=embed)
        await msg.clear_reactions()

        break
        
    return



def setup(bot):
  bot.add_cog(cogGame(bot))