import discord

def get_instagram_embed(insta_handle,insta_url,about,image_url,footer):
  embed=discord.Embed(title=insta_handle,url = insta_url , description=about, color=0x640616)
  embed.set_author(name='INSTAGRAM')
  embed.set_thumbnail(url='https://image.flaticon.com/icons/png/512/174/174855.png')
  embed.set_footer(text=footer)
  if not image_url:
    embed.set_image(url=image_url)
  return embed

def get_facebook_embed(facebook_name, facebook_url, about, image_url, footer):
  embed=discord.Embed(title=facebook_name,url = facebook_url , description=about, color=0x3b5998)
  embed.set_author(name='INSTAGRAM')
  embed.set_thumbnail(url='https://image.flaticon.com/icons/png/512/174/174848.png')
  embed.set_footer(text=footer)
  if not image_url:
    embed.set_image(url=image_url)
  return embed
  
  