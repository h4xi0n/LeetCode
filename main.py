import os
import discord
from keep_alive import keep_alive
import time
import requests
import json

welcome_message = 'Hello!, \nWelcome to LEET Store, Hope you enjoy your stay. Raise a ticket to request our services.\n\nType: ```!leet boost [Current Rank] [Target Rank]``` to calculate boosting (only available in tickets)\n\nType: ```!leet instagram``` to get our instagram link.\n\nType: ```!leet tell me about [@mention]``` for complimenting a user.'

channel_welcome_help = '```Hello, \nWelcome to LEET Store, We are happy to help you\nFor our best in class boosting services please type !leet boost <current rank> <target rank>\nEG: !leet boost P1 D1\nUse abbrevations like G1 for Gold 1 and P1 for Platinum 1. (IM for Immortal && RA for Radiant)```'

result_prefix = '@here\n\n```Breakdown: \n\n'
result_suffix = '\n\nFollow us on Instagram: @theleetstore(https://www.instagram.com/theleetstore/).\n\nA booster will be assigned by our team as soon as payment is done.\n\nThank you for choosing our services.\n\nYou can view our vouches to verify our trust factor at <#806988441740115989>\n\nYou can make payments via <#840083989410742282>'

leetcode = os.environ['TOKEN']
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
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for !leet'))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content == '!leet':
    await message.channel.send(welcome_message)
    return
  if message.content == '!leet instagram':
    await message.channel.send('https://www.instagram.com/theleetstore/')
    return

  if 'ticket' in message.channel.name:
    if message.content.lower().startswith('!leet tell me about '):
      user = message.mentions[0].mention
      await message.channel.send(get_compliment(user))
      
    if message.content.lower().startswith('!leet insult '):
      user = message.mentions[0].mention
      await message.channel.send(get_insult(user))
      
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
        
        embed=discord.Embed(title="Total Amount: "+str(final_amount)+'Rs.', description="Here's the rate breakdown as follows:", color=0xd40202)
        breakdown(rankset[1],rankset[2],embed)
        embed.set_author(name="THE LEET STORE")
        embed.set_thumbnail(url="https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt08d90f64fcde633b/5ed179454d187c101f3f3124/Tactibear.gif")
        embed.set_footer(text="Instagram: @theleetstore")
        embed.add_field(name='Service Charge: ', value=str(service_charge)+'Rs.', inline=False)
        embed.add_field(name='Check out our vouches at:',value='<#806988441740115989>',inline=False)
        embed.add_field(name='Payment can be done via:',value='UPI: valorantboosting@ybl\n\tOR\nQR Code below.',inline=False)
        embed.set_image(url=os.environ['IMGURL'])
        await message.channel.send(content='\n@here\nHere\'s the boosting details.\nA Manager or Support will assgin you a Booster as soon as payment is done.',embed=embed)
        #await message.channel.send(result_prefix+breakdowns+'\nService Charges = '+str(service_charge)+'Rs.'+'\n\nTotal amount = '+str(final_amount)+'Rs.```'+result_suffix)
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
    time.sleep(2)
    await channel.send(channel_welcome_help)
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

def get_compliment(user):
  response = requests.get('https://complimentr.com/api')
  json_data = json.loads(response.text)
  compliment = json_data['compliment']
  if 'you are' in compliment:
    print('you are')
    compliment = replace(compliment,'you are',user+' is')
  if 'you' in compliment:
    print('you')
    compliment = replace(compliment,'you',user)
  return compliment

def get_insult(user):
  response = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
  json_data = json.loads(response.text)
  insult = json_data['insult']
  return 'Hey '+user+', '+insult
  
def replace(line, word, new_word):
    new_line = line
    for i in range(line.count(word)):
        start_index = new_line.find(word) #returns the starting index of the word
        new_line = new_line[:start_index] + new_word + new_line[start_index + len(word):]
    return new_line

keep_alive()
client.run(leetcode)