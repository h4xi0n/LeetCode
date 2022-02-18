import os
import discord
import time
from datetime import datetime
import pytz
import annoy_people
import social_embed
import account_value_calculator
import discord.utils
from discord.utils import get
import upload_img
#from discord.utils import get
intents = discord.Intents.all()
intents.members = True
intents.guilds = True
intents.reactions = True

client = discord.Client(intents=intents)
#client= commands.Bot(command_prefix="!", intents=intents)
today = datetime.now(tz=pytz.timezone("Asia/Kolkata"))
rate_array = [30,
40,
50,
60,
70,
80,
95,
130,
150,
179,
220,
275,
330,
430,
550,
750,
1250,
1750,
3000,
3500,
7000]

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
'IM1',
'IM2',
'IM3',
'RA'
]

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for !leet | @theleetstore'))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  
  role_array = ['806981872147496960','827800439985799228','806981021726670910']
  author_roles = [str(y.id) for y in message.author.roles]
  
  if not any(x in role_array for x in author_roles) and not 'ticket' in message.channel.name and not 'vouch-for-us' in message.channel.name:
    if 'boosting' in message.content.lower() or 'boost' in message.content.lower() or 'rank push' in message.content.lower() or 'pushing rank' in message.content.lower() or 'rank pushing' in message.content.lower():
      channel = client.get_channel(933741314330202143)
      warnembed = discord.Embed(title='LEET BOT WARNINGS',description = message.author.name+' has been messaged personally regarding our boosting service',color=0x3b5998)
      warnembed.add_field(name='His message content from channel '+message.channel.name,value=message.content)
      
      await channel.send(embed=warnembed)
      await message.delete()
      await message.author.send("Please use <#826553291051499591> to raise a ticket and request for our boosting service. Our boosting rates are <#806985172049723422>")


  if ('vouch-for-us' in message.channel.name and message.content.startswith('!anon')) or any(x in role_array for x in author_roles):
    vouch_embed = discord.Embed(title='VOUCH POST', description ='This post is done by a customer who wants to stay anonymous')
    vouch_embed.add_field(name='Vouch message',value=message.content.replace('!anon ',''))
    vouch_embed.set_author(name="THE LEET STORE")

  if 879553156432945233 == message.channel.id and not message.content.startswith('!leet estimate'):
    message.delete()

  if message.content.startswith('..') and any(x in role_array for x in author_roles):
    god_message = message.content.replace("..","")
    await message.delete()
    await message.channel.send(god_message)

  if message.content == '!leet' or message.content == '!leet help':
    helpembed = discord.Embed(title='LEET BOT HELP', description= 'Hello, welcome to the THE LEET STORE.\nUse the below commands to get help from our bot', color=0x3b5998)
    helpembed.add_field(name='Our Instagram:', value='cmd: !leet insta\n\n', inline=False)
    helpembed.add_field(name='Compliment Someone:', value='cmd: !leet tell me about @mention\n\nExample:\n!leet tell me about @ADS\n-------------------------------------\n', inline=False)
    helpembed.add_field(name='Boosting Request:', value='cmd: !leet boost <curr_rank> <target_rank>\n(Will only work inside tickets <#826553291051499591>)\n\nExample:\n!leet boost g1 d1\n-------------------------------------\n', inline=False)
    helpembed.add_field(name='Estimate your account value:', value='cmd: !leet estimate <your account skin list>\n(One item per line)\n(only works on <#879553156432945233>)\n\nExample:\n !leet estimate\nGlitchpop dagger\nElderflame Bundle\n6 x bp\nValorantGo knife\nPrime Vandal\n1000 VP\n-------------------------------------\n', inline=False)
    helpembed.set_thumbnail(url='https://i.imgur.com/Eo2IzAc.png')
    await message.channel.send(embed=helpembed)
    return

  if message.content.lower().startswith('!add ') and any(x in role_array for x in author_roles):
    user = message.mentions[0]
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    overwrite.read_messages = True
    overwrite.attach_files = True
    overwrite.read_message_history = True
    await message.channel.set_permissions(user, overwrite=overwrite)
    time.sleep(4)
    booster_embed = discord.Embed(title = 'Booster Details ', description = 'Your booster will be '+user.name+', He will help you reach the rank you desire in no time.', color=0x3b5998)
    booster_embed.set_author(name="THE LEET STORE")
    booster_embed.set_thumbnail(url="https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt08d90f64fcde633b/5ed179454d187c101f3f3124/Tactibear.gif")
    booster_embed.set_footer(text="Instagram: @theleetstore")
    await message.delete()
    await message.channel.send(embed=booster_embed)

  if message.content.lower().startswith('!remove ') and any(x in role_array for x in author_roles):
    user = message.mentions[0]
    ticket_channel = message.channel
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    overwrite.read_messages = False
    overwrite.attach_files = False
    overwrite.read_message_history = False
    await ticket_channel.set_permissions(user, overwrite=overwrite)

  if message.content.lower().startswith('!pay'):
    payembed = discord.Embed(title = 'Payment Details ', description = 'Use the below methods to make your payments', color=0x3b5998)
    payembed.add_field(name='Check out our vouches at:',value='<#806988441740115989>',inline=False)
    payembed.add_field(name='UPI',value='\nvalorantboosting@ybl',inline=False)
    payembed.add_field(name='QR CODE',value='QR Code:(click to enlarge)',inline=False)
    payembed.set_image(url=os.environ['IMGURL'])
    payembed.set_author(name="THE LEET STORE")
    payembed.set_thumbnail(url="https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt08d90f64fcde633b/5ed179454d187c101f3f3124/Tactibear.gif")
    payembed.set_footer(text="Instagram: @theleetstore")
    await message.delete()
    await message.channel.send(embed=payembed)

  if message.content.lower().startswith('!sale'):
    await message.delete()
    await message.channel.send(embed=get_account_sale_embed())


  if message.content.startswith('!leet estimate') and ('know-valo-account-value' in message.channel.name or any(x in role_array for x in author_roles)):
    if(message.content.endswith('!leet estimate')):
      return
    
    extra_vp,melee_amt,skin_amt,bundle_amt,bp_amt = account_value_calculator.calculate_total_vp(str(message.content.replace('estimate','estimate\n')))
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
    valembed.add_field(name='TOTAL ESTIMATED WORTH: ', value=str(int(estimate_amount_spent))+' Rs.', inline=False)
    valembed.set_author(name='THE LEET STORE')
    valembed.set_footer(text="(This bot is still in beta, do report if any issues noticed.)\n*Rates exclude Battlepass skins, Rank value, Player card value or Radianite point value etc.\n*VP rates are subject to change in future.\n*Above value is just an estimate from average price of a single valorant point.\nInstagram: @theleetstore")
    valembed.set_thumbnail(url='https://i.imgur.com/Eo2IzAc.png')
    valembed.add_field(name='You can download & share the image below: ', value='(Click to enlarge -> Right Click -> Open Link to Download)', inline=False)
    img_url=account_value_calculator.embed_result_to_image(extra_vp,melee_amt,skin_amt,bundle_amt,bp_amt,total_vp_spent,int(estimate_amount_spent))
    valembed.add_field(name='Image URL ', value=str(upload_img.shorten(img_url)), inline=False)
    valembed.set_image(url=img_url)
    time.sleep(3)
    await message.channel.send(embed=valembed)

  if message.content == '!leet insta':
    await message.channel.send(embed = social_embed.get_instagram_embed('@theleetstore','https://www.instagram.com/theleetstore/','Hardstuck? Dm us!\nWe can help!\nWe have 20+ pro diamond/immortal boosters.\nOur vouches (in discord) shows our quality of work.','https://i.imgur.com/HcqZzKN.png','THE LEET STORE'))
    return
  if message.content.lower().startswith('!leet tell me about '):
    user = message.mentions[0].mention
    await message.channel.send(annoy_people.get_compliment(user))
      
  if message.content.lower().startswith('!leet insult '):
    user = message.mentions[0].mention
    await message.channel.send(annoy_people.get_insult(user))

  if message.mention_everyone and not any(x in role_array for x in author_roles):
    await message.author.send('Please do not mention everyone or here in THE LEET STORE! You have been warned!')
    await message.delete()

  if 'ticket' in message.channel.name or any(x in role_array for x in author_roles):
    if message.content.lower().startswith('!boost finished') or message.content.lower().startswith('!bf'):
      boostembed=discord.Embed(title="Your boosting is completed. We hope you're happy with our services. Let us know if you need any more help.", description="Thank you for using our services", color=0xd40202)
      boostembed.add_field(name='Do vouch for us if you liked our support & services.',value='<#806988441740115989>',inline=False)
      boostembed.set_footer(text="Instagram: @theleetstore")
      boostembed.set_thumbnail(url="https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt08d90f64fcde633b/5ed179454d187c101f3f3124/Tactibear.gif")
      await message.delete()
      await message.channel.send(embed=boostembed)

    if '!con' in message.content.lower():
      await message.delete()
      await message.channel.send("50Rs extra per condition/rule.")


    if message.content.lower().startswith('!pr'):
      recembed = discord.Embed(title='Payment Received.',description='Thank you for trusting in our services, a booster will be assigned as soon as possible! Feel free to share your credentials here. It\'s safe.',color=0xd40202)
      recembed.set_footer(text="Instagram: @theleetstore")
      recembed.set_thumbnail(url="https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt08d90f64fcde633b/5ed179454d187c101f3f3124/Tactibear.gif")
      role = get(message.guild.roles, name="Active Customers")
      if message.mentions:
        user_id = message.mentions[0].id
        member = message.guild.get_member(user_id)
        print(member)
        print(role)
        await member.add_roles(role)
      await message.delete()
      await message.channel.send(embed=recembed)

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
        
        razer = message.guild.get_member(224221471743016963)
        transcript_channel = message.guild.get_channel(938542775710933072)
        channel_msg = "```"+"\nDate\t\t\t\t\t:"+today.strftime("%d/%m/%Y %H:%M:%S")+"\nCustomer\t\t\t\t:"+message.author.name+"\nChannel \t\t\t\t:"+message.channel.name+"\nRank\t\t\t\t\t:"+rankset[1].upper()+" to "+rankset[2].upper()+"\nBooster Fee \t\t\t:"+str(rank_amount)+"Rs."+"\nService Charge  \t\t:"+str(service_charge)+"Rs.(18%)"+"\nTotal Amount\t\t\t:"+str(final_amount)+"Rs.```"
        
        await razer.send(channel_msg)
        
        await transcript_channel.send(channel_msg)


        embed=discord.Embed(title="Total Amount: "+str(final_amount)+'Rs.', description="Here's the rate breakdown:", color=0xd40202)
        breakdown(rankset[1],rankset[2],embed,service_charge)
        if 'bot' in message.channel.name: 
          await message.channel.send(embed=embed)
        else:
          embed.set_author(name="THE LEET STORE")
          embed.set_thumbnail(url="https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt08d90f64fcde633b/5ed179454d187c101f3f3124/Tactibear.gif") 
          embed.set_footer(text="Note: Our rates have been reduced, There will be a small delay in our services due to abundant amount of service requests.\nA minor service charge has been added.\nYour rank will be boosted by esports level players on depending rank. \nInstagram: @theleetstore")
          embed.add_field(name='Check out our vouches at:',value='<#806988441740115989>',inline=False)
          embed.add_field(name='Payment can be done via:',value='\nUPI: valorantboosting@ybl\nQR Code:(click to enlarge)',inline=False)
          embed.set_image(url=os.environ['IMGURL'])
          await message.channel.send(content='\nHello '+message.author.mention+','+'\nHere\'s the boosting details.\nA <@&806981872147496960> or <@&827800439985799228> will assgin you a booster as soon as payment is done.',embed=embed)
      except Exception as e:
        print(e)
        await message.channel.send('```Error Please try again!\nPlease enter the correct syntax. ie.\nformat: !leet boost <currentrank> <targetrank>\nUse abbrevations like G1 for Gold 1 and P1 for Platinum 1. (IM1 for Immortal 1 && RA for Radiant)\n\nExample:\n!leet boost g1 d1```')
    else:
      return
  else:
    return


@client.event
async def on_guild_channel_create(channel):
  print(channel.name)
  if 'ticket' in channel.name:
    time.sleep(4)
    async for messages in channel.history(limit = 1):
      await channel.edit(name=channel.name+'_['+messages.mentions[0].name+']')
      
    welcome_embed = discord.Embed(title='How to request our top-notch boosting service', description='Use the below command to request \nfor our boosting service', color=0xd40202)
    welcome_embed.set_thumbnail(url="https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt08d90f64fcde633b/5ed179454d187c101f3f3124/Tactibear.gif")
    welcome_embed.set_author(name="THE LEET BOOSTING SERVICE")
    welcome_embed.add_field(name='Command format: ',value='!leet boost <currentrank> <targetrank>',inline=False)
    welcome_embed.add_field(name ='Example:',value='!leet boost g1 d1',inline = False)
    welcome_embed.add_field(name ='Our rate sheet:',value='(click to enlarge image)',inline = False)
    welcome_embed.set_image(url='https://media.discordapp.net/attachments/806985172049723422/929952429871616021/NEWLEETNOTICE-January_New_Act.png')
    welcome_embed.set_footer(text="Extra 50Rs/Rule or Condition\nUse abbrevations like G1 for Gold 1 and P1 for Platinum 1. \n(IM2 for Immortal 2 && RA for Radiant)")
    await channel.send(embed = welcome_embed)

    #await channel.edit(name=channel.name+' ['++']')
  return

def get_account_sale_embed():
    acc_sale_embed = discord.Embed(title='For account sales please use the following channels', description='The LEET Store does not sell your account personally, We only do middleman service for a minor fee',color=0xd40202)
    acc_sale_embed.set_author(name="THE LEET STORE")
    acc_sale_embed.set_thumbnail(url="https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt08d90f64fcde633b/5ed179454d187c101f3f3124/Tactibear.gif")
    acc_sale_embed.add_field(name ='Valorant Account Sales',value='<#806996090284539904>',inline=False)
    acc_sale_embed.add_field(name ='Steam Account and Inventory Trade', value= '<#902796038706962504>',inline=False)
    acc_sale_embed.add_field(name ='Market for any other random stuff',value='<#902796088933744661>',inline=False)
    acc_sale_embed.add_field(name ='Valorant accounts by The LEET Store',value ='<#855139318300147773>',inline=False)
    acc_sale_embed.set_footer(text='Follow us on instagram @theleetstore / @valorant.boosters')
    print(acc_sale_embed)
    return acc_sale_embed


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

def breakdown(start_rank,end_rank,embed,service_charge):
  start_index = rank_array.index(start_rank.upper())
  end_index = rank_array.index(end_rank.upper())
  breaked_down_data = ""
  
  sub_rank_array = rank_array[start_index:end_index+1]
  sub_rate_array = rate_array[start_index:end_index]
  broken_sc = int(service_charge/len(sub_rate_array))
  i = 0
  for rate in sub_rate_array:
    current_rank = sub_rank_array[i]
    next_rank = sub_rank_array[i+1]
    i=i+1
    embed.add_field(name=current_rank+' to '+next_rank+': ',value = str(rate+broken_sc)+'Rs.', inline=True)
    breaked_down_data = breaked_down_data + current_rank+' to '+next_rank+' = '+str(rate)+'Rs\n'
    if sub_rate_array.index(rate) == len(sub_rate_array):
      break
  return breaked_down_data

def get_service_charge(amount):
  service_charge = amount * .18
  return int(service_charge)

def get_discord_client():
  return client