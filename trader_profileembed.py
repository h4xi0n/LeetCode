import discord

trader_embed = discord.Embed(title='LEET TRADER PROFILE', description= 'This is the discord profile of a trader within our server. Do vouch for them if you feel that they are trusted or has done trade with them. This does not prove that THE LEET STORE will consider the trader trusted.', color=0x3b5998)


def initembed():
  trader_embed = discord.Embed(title='LEET TRADER PROFILE', description= 'This is the discord profile of a trader within our server. Do vouch for them if you feel that they are trusted or has done trade with them. This does not prove that THE LEET STORE will consider the trader trusted.', color=0x3b5998)

def set_details(user, instagram_id, discord_id, real_name):

  trader_embed.add_field(name='Discord ID', value='cmd: !leet insta\n\n', inline=False)
  trader_embed.add_field(name='Instagram ID', value='cmd: !leet insta\n\n', inline=False)
  trader_embed.add_field(name='Real Name', value='cmd: !leet insta\n\n', inline=False)


