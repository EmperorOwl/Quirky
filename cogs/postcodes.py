import discord
import asyncio
from discord.ext import commands
from datetime import datetime



# <-----------------[COG POSTCODES]------------------> #

class cogPostcodes(commands.Cog, name="Postcodes"):



  def __init__(self, bot):
    self.bot = bot

  

  # <----------------[GRP POSTCODES]-----------------> #

  @commands.group(
    name = 'postcodes',
    description = "View and find postcodes!",
    aliases = ['pcs']
  )
  async def grpPostcodes(self, ctx):
    
    if ctx.invoked_subcommand is None:

      content = f"**✉️  |  {ctx.author.name}**, incorrect subcommand passed!\n*Use either `postcodes view` or `postcodes find`.*"

      await ctx.send(content=content)

    return



  # <-------------------[CMD VIEW]-------------------> #

  @grpPostcodes.command(name='view')
  async def cmdView(self, ctx, page_num=None):

    if page_num == None:
      page_num = 0
    else:
      page_num = int(page_num) - 1


    def genEmbed(page_num):

      embed = discord.Embed(
        title = f"Postcodes (Page {page_num + 1} of {len(paginator.pages)})",
        description = paginator.pages[page_num],
        color = discord.Colour.blue(),
        timestamp = datetime.now()
      )

      embed.set_footer(
        text = "Data from Australia Post"
      )

      return embed
    
    postcodes_file = open("postcodes.txt", "r")
    paginator = commands.Paginator(max_size=250)
    for line in postcodes_file:
      paginator.add_line(line.replace("\n", ""))
    postcodes_file.close()
      
    msg = await ctx.send(embed=genEmbed(page_num))

    await msg.add_reaction('◀️')
    await msg.add_reaction('▶️')


    while True:

      def check(reaction, user):
        return (    reaction.message.id == msg.id 
                and user.name != self.bot.user.name    )
      
      try:

        reaction, user = await self.bot.wait_for(
          'reaction_add',
          timeout = 120,
          check = check
        )

        emoji = str(reaction.emoji)
        await msg.remove_reaction(reaction, user) 

        if emoji == '◀️' and page_num > 0:
      
          page_num -= 1
          embed = genEmbed(page_num)

          await msg.edit(embed=embed)

        elif emoji == '▶️' and page_num < (len(paginator.pages) - 1):
          
          page_num += 1
          embed = genEmbed(page_num)
          
          await msg.edit(embed=embed)

      except asyncio.TimeoutError:
        
        await msg.clear_reactions()

        break

    return

  

  # <-------------------[CMD FIND]-------------------> #
  
  @grpPostcodes.command(name='find')
  async def cmdFind(self, ctx, *, search):

    postcodes_file = open('postcodes.txt', 'r')

    try: # searching for postcode's suburb

      search = int(search)
      search = str(search) # convert back to string


      suburbs = []
      for line in postcodes_file:
        
        suburb = line.split(", ")[0].title()
        postcode = line.split(", ")[1].replace("\n", "")

        if (    search in line 
            and len(search) == len(postcode)
        ):

          suburbs.append(suburb)


      if len(suburbs) == 1:

        content = f"The suburb with postcode `{search}` is **{suburbs[0]}**."

      elif len(suburbs) > 1:

        content = f"The suburbs with postcode `{search}` are {', '.join(f'**{s}**' for s in suburbs)}."
      
      else:

        content = f"No suburb matched that postcode."  

      await ctx.send(content=content)

    except ValueError: # searching for suburb's postcode
      
      postcodes = []
      for line in postcodes_file:
        
        suburb = line.split(", ")[0]
        postcode = line.split(", ")[1].replace("\n", "")
        
        if (    search.upper() in line 
            and len(search) == len(suburb)
        ):

          postcodes.append(postcode)


      if len(postcodes) == 1:

        content = f"The postcode for suburb **{search.title()}** is `{postcodes[0]}`."

      elif len(postcodes) > 1:

        content = f"The postcodes for suburb **{search.title()}** are {', '.join(f'`{p}`' for p in postcodes)}."
      
      else:

        content = f"No postcode matched that suburb."  

      await ctx.send(content=content)

    postcodes_file.close()

    return



  # <-------------------[CMD ADD]--------------------> #

  @grpPostcodes.command(name='add')
  @commands.is_owner()
  async def cmdAdd(self, ctx, new_suburb, new_postcode: int):
    
    # check whether suburb already exists

    postcodes_file = open('postcodes.txt', 'r')
    for line in postcodes_file:

      suburb = line.split(", ")[0]
      
      if (    new_suburb.upper() in line 
          and len(new_suburb) == len(suburb)
      ):

        content = f"**{new_suburb.title()}** already exists!"

        await ctx.send(content=content)

        return


    # add new suburb

    postcodes_file = open('postcodes.txt', 'a')
    postcodes_file.write(f"{new_suburb.upper()}, {new_postcode}\n")
    postcodes_file.close()

    content = f"New entry added: **{new_suburb.upper()}**, `{new_postcode}`"

    await ctx.send(content=content)

    return

  

  # <------------------[CMD DELETE]------------------> #

  @grpPostcodes.command(name='delete')
  @commands.is_owner()
  async def cmdDelete(self, ctx, *, target_suburb):
    
    postcodes_file = open('postcodes.txt', 'r')
    lines = postcodes_file.readlines()
    line_num = 0
    for line in lines:
        
        suburb = line.split(', ')[0]
        
        if (    target_suburb.upper() in line 
            and len(target_suburb) == len(suburb)
        ):

          del lines[line_num]

        line_num += 1
  
    postcodes_file.close()

    new_postcodes_file = open('postcodes.txt', 'w')

    for line in lines:
      new_postcodes_file.write(line)

    new_postcodes_file.close()

    content = f"**{target_suburb.title()}** has been deleted."

    await ctx.send(content=content)

    return
    


def setup(bot):
  bot.add_cog(cogPostcodes(bot))