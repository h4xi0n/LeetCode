import os
import discord
import time
import annoy_people
import social_embed
import account_value_calculator

client = discord.Client()
rate_array = [100,
100,
175,
175,
175,
200,
200,
200,
450,
450,
450,
750,
750,
750,
1500,
1500,
1500,
3500,
10000]

rank_array = ['I1',
'I2',
'I3',
'B1',
'B2',
'B3',
'S1',
'S2',
'S3',
'G1',
'G2',
'G3',
'P1',
'P2',
'P3',
'D1',
'D2',
'D3',
'IM',
'RA'
]

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for !leet | @theleetstore'))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content == '!leet' or message.content == '!leet help':
    helpembed = discord.Embed(title='LEET BOT HELP', description= 'Hello, welcome to the THE LEET STORE.\nUse the below commands to get help from our bot', color=0x3b5998)
    helpembed.add_field(name='Our Instagram:', value='cmd: !leet insta\n\n', inline=False)
    helpembed.add_field(name='Compliment Someone:', value='cmd: !leet tell me about @mention\n\nExample:\n!leet tell me about @ADS\n-------------------------------------\n', inline=False)
    helpembed.add_field(name='Boosting Request:', value='cmd: !leet boost <curr_rank> <target_rank>\n(Will only work inside tickets <#826553291051499591>)\n\nExample:\n!leet boost g1 d1\n-------------------------------------\n', inline=False)
    helpembed.add_field(name='Estimate your account value:', value='cmd: !leet estimate <your account skin list>\n(One item per line)\n(only works on <#879553156432945233>)\n\nExample:\n !leet estimate\nGlitchpop dagger\nElderflame Bundle\n6 x bp\nValorantGo knife\nPrime Vandal\n1000 VP\n-------------------------------------\n', inline=False)
    helpembed.set_thumbnail(url='https://i.imgur.com/Eo2IzAc.png')
    await message.channel.send(embed=helpembed)
    return

  if message.content.startswith('!leet estimate') and 'know-your-account-value' in message.channel.name:
    extra_vp,melee_amt,skin_amt,bundle_amt,bp_amt = account_value_calculator.calculate_total_vp(str(message.content))
    total_vp_spent = extra_vp + melee_amt + skin_amt + bundle_amt + bp_amt
    estimate_amount_spent = total_vp_spent * float(os.environ['CONVERSION'])
    print(total_vp_spent)

    valembed=discord.Embed(title='Account Value Estimation', description= 'Below is the total vp and account value of the mentioned skins.\nUse our <#806996090284539904> to sell/trade accounts.\nPlease follow <#856188052308623360>.', color=0x3b5998)
    valembed.add_field(name='KNIFE: ', value=str(melee_amt)+' VP', inline=True)
    valembed.add_field(name='GUN SKINS: ', value=str(skin_amt)+' VP', inline=True)
    valembed.add_field(name='BUNDLES: ', value=str(bundle_amt)+' VP', inline=True)
    valembed.add_field(name='BATTLEPASS: ', value=str(bp_amt)+' VP', inline=True)
    valembed.add_field(name='EXTRA VP: ', value=str(extra_vp)+' VP', inline=True)
    valembed.add_field(name='TOTAL VALORANT POINTS SPENT: ', value=str(total_vp_spent)+' VP', inline=False)
    valembed.add_field(name='TOTAL ESTIMATED WORTH: ', value=str(estimate_amount_spent)+' Rs.', inline=False)
    valembed.set_author(name='THE LEET STORE')
    valembed.set_footer(text="(This bot is still in beta, do report if any issues noticed.)\n*Rates exclude Battlepass skins, Rank value, Player card value or Radianite point value etc.\n*VP rates are subject to change in future.\n*Above value is just an estimate from average price of a single valorant point.\nInstagram: @theleetstore")
    valembed.set_thumbnail(url='https://i.imgur.com/Eo2IzAc.png')
    await message.channel.send(embed=valembed)

  if message.content == '!leet tryhard1! killbot':
    await message.channel.send('I\'m suiciding! Good bye, cruel world!')
    await client.close()
    exit()

  if message.content == '!leet insta':
    await message.channel.send(embed = social_embed.get_instagram_embed('@theleetstore','https://www.instagram.com/theleetstore/','Hardstuck? Dm us!\nWe can help!\nWe have 20+ pro diamond/immortal boosters.\nOur vouches (in discord) shows our quality of work.','https://i.imgur.com/HcqZzKN.png','THE LEET STORE'))
    return
  if message.content.lower().startswith('!leet tell me about '):
    user = message.mentions[0].mention
    await message.channel.send(annoy_people.get_compliment(user))
      
  if message.content.lower().startswith('!leet insult '):
    user = message.mentions[0].mention
    await message.channel.send(annoy_people.get_insult(user))

  role_array = ['806981872147496960','827800439985799228','806981021726670910']
  author_roles = [str(y.id) for y in message.author.roles]
  if 'ticket' in message.channel.name or any(x in role_array for x in author_roles):
    if message.content.lower().startswith('!leet boost'):
      try:
        rankset = message.content[11:None].split(' ')
        
        rank_amount = calculate_rate(rankset[1],rankset[2])
        if rank_amount == -1:
          await message.channel.send('```Please enter Current Rank and Target Rank.\nformat: !leet boost <currentrank> <targetrank>```')
          return
        if rank_amount == 1:
          await message.channel.send('Current Rank is higher than Target Rank')
          return
      
        service_charge = get_service_charge(rank_amount)
        final_amount = service_charge + rank_amount
        
        embed=discord.Embed(title="Total Amount: "+str(final_amount)+'Rs.', description="Here's the rate breakdown:", color=0xd40202)
        breakdown(rankset[1],rankset[2],embed)
        embed.set_author(name="THE LEET STORE")
        embed.set_thumbnail(url="https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt08d90f64fcde633b/5ed179454d187c101f3f3124/Tactibear.gif")
        embed.set_footer(text="Instagram: @theleetstore")
        embed.add_field(name='Service Charge: ', value=str(service_charge)+'Rs.', inline=False)
        embed.add_field(name='Check out our vouches at:',value='<#806988441740115989>',inline=False)
        embed.add_field(name='Payment can be done via:',value='\nUPI: valorantboosting@ybl\nQR Code:(click to enlarge)',inline=False)
        embed.set_image(url=os.environ['IMGURL'])
        await message.channel.send(content='\nHello '+message.author.mention+','+'\nHere\'s the boosting details.\nA <@&806981872147496960> or <@&827800439985799228> will assgin you a <@&806981021726670910> as soon as payment is done.',embed=embed)
      except Exception as e:
        print(e)
        await message.channel.send('```Error Please try again!\nPlease enter Current Rank and Target Rank.\nformat: !leet boost <currentrank> <targetrank>\nUse abbrevations like G1 for Gold 1 and P1 for Platinum 1. (IM for Immortal && RA for Radiant)```')
    else:
      return
  else:
    return


@client.event
async def on_guild_channel_create(channel):
  print(channel.name)
  if 'ticket' in channel.name:
    time.sleep(4)
    welcome_embed = discord.Embed(title='How to request our top-notch boosting service', description='Use the below command to request \nfor our boosting service', color=0xd40202)
    welcome_embed.set_thumbnail(url="https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt08d90f64fcde633b/5ed179454d187c101f3f3124/Tactibear.gif")
    welcome_embed.set_author(name="THE LEET BOOSTING SERVICE")
    welcome_embed.add_field(name='Command format: ',value='!leet boost <currentrank> <targetrank>',inline=False)
    welcome_embed.add_field(name ='Example:',value='!leet boost g1 d1',inline = False)
    welcome_embed.add_field(name ='Our rate sheet:',value='(click to enlarge image)',inline = False)
    welcome_embed.set_image(url='https://i.imgur.com/HcqZzKN.png')
    welcome_embed.set_footer(text="Use abbrevations like G1 for Gold 1 and P1 for Platinum 1. \n(IM for Immortal && RA for Radiant)")
    await channel.send(embed = welcome_embed)
  return
  

def calculate_rate(start_rank,end_rank):
  print('Calculating rates')
  start_index = rank_array.index(start_rank.upper())
  end_index = rank_array.index(end_rank.upper())
  total_amount = 0
  if start_index == None and end_index == None:
    print('-1')
    return -1
  if end_index <= start_index:
    print('1')
    return 1
  sub_rate_array = rate_array[start_index:end_index]
  for amount in sub_rate_array:
    total_amount = total_amount+amount
  return total_amount

def breakdown(start_rank,end_rank,embed):
  start_index = rank_array.index(start_rank.upper())
  end_index = rank_array.index(end_rank.upper())
  breaked_down_data = ""
  sub_rank_array = rank_array[start_index:end_index+1]
  sub_rate_array = rate_array[start_index:end_index]
  i = 0
  for rate in sub_rate_array:
    current_rank = sub_rank_array[i]
    next_rank = sub_rank_array[i+1]
    i=i+1
    embed.add_field(name=current_rank+' to '+next_rank+': ',value = str(rate)+'Rs.', inline=True)
    breaked_down_data = breaked_down_data + current_rank+' to '+next_rank+' = '+str(rate)+'Rs\n'
    if sub_rate_array.index(rate) == len(sub_rate_array):
      break
  return breaked_down_data

def get_service_charge(amount):
  if amount > 2000:
    amount = 100
    return amount
  if amount > 1000:
    amount = 50
    return amount
  if amount > 500:
    amount = 25
    return amount
  else:
    amount = 15
    return amount

def get_discord_client():
  return client