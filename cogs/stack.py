import asyncio
from discord.ext import commands
from collections import deque



# <-------------------[COG STACK]--------------------> #

class cogStack(commands.Cog, name="Stack Simulator"):



  def __init__(self, bot):
    self.bot = bot



  # <------------------[CMD STACK]-------------------> #

  @commands.command(
    name = 'stack',
    description = "Stack some coins!"
  )
  async def cmdStack(self, ctx):

    from modules.stack import getStackEmbed

    coin_emojis = [
      self.bot.get_emoji(820160827586773033), # 5c
      self.bot.get_emoji(820160840526200862), # 10c
      self.bot.get_emoji(820160842913939458), # 20c
      self.bot.get_emoji(820160840091041802), # 50c
      self.bot.get_emoji(820160840186462229), # 100c
      self.bot.get_emoji(820160831899041812), # 200c
    ]

    pop_emoji = self.bot.get_emoji(820195693179174912)

    box_emoji = self.bot.get_emoji(820178590515068938)

    stack = deque()
    
    msg = await ctx.send(embed=getStackEmbed(stack, box_emoji))

    for c in coin_emojis: await msg.add_reaction(c)

    await msg.add_reaction(pop_emoji)

    while True:

      def check(reaction, user):
        return reaction.message.id == msg.id and user.name != self.bot.user.name
      
      try: 

        reaction, user = await self.bot.wait_for(
          'reaction_add',
          timeout = 300, 
          check = check
        )

        await msg.remove_reaction(reaction, user)


        # user reacts with one of the six coins
        if reaction.emoji in coin_emojis:

          if len(stack) < 5:

            stack.appendleft(reaction.emoji)
            await msg.edit(embed=getStackEmbed(stack, box_emoji))
          
          else:

            await ctx.send(f"{ctx.author.mention} the stack is full! Pop a coin before pushing the next coin.")
        
        # user reacts with pop
        if reaction.emoji == pop_emoji:

          if len(stack) > 0:

            stack.popleft()
            await msg.edit(embed=getStackEmbed(stack, box_emoji))

          else:

            await ctx.send(f"{ctx.author.mention} the stack is empty! Push a coin before popping the next coin.")

      except asyncio.TimeoutError:

        await msg.clear_reactions()

        break

    return



def setup(bot):
  bot.add_cog(cogStack(bot))