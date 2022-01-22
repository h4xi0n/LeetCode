import json
import re
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import upload_img

def retrieve_data():
  data = open('skindata.json','r').read().lower()
  json_data = json.loads(data)
  return json_data

def get_bundle():
  json_data = retrieve_data()
  bundle_object = json_data['bundle']
  return bundle_object

def get_skins():
  json_data = retrieve_data()
  skin_object = json_data['skins']
  return skin_object

def get_melees():
  json_data = retrieve_data()
  melee_object = json_data['melee']
  return melee_object

def get_list_of_items(message):
  bundle_list = []
  skin_list = []
  melee_list = []
  if '\n' in message:
    lines_split = message.lower().split('\n') 
  else:
    lines_split = message.lower()
  battlepass_count = []
  extra_vp = 0
  for item in lines_split:
    if item.strip().endswith('battlepass') or item.strip().endswith('bp') or item.strip().endswith('pass'):
      battlepass_count = int(re.search(r'\d+', item).group())
      if item.strip().startswith('all'):
        battlepass_count = 8
      #[int(s) for s in item.split() if s.isdigit()]
    elif item.strip().endswith('vp') or ('radianite' not in item and item.strip().endswith('points')):
      extra_vp = int(re.search(r'\d+', item).group())
      #[int(s) for s in item.split() if s.isdigit()][0]
    elif item.strip().endswith('bundle'):
      item_list1 = item.split(' ')
      for bundle_item in item_list1:
        bundle_list.append(bundle_item)
    elif item.strip().endswith('melee') or item.strip().endswith('knife') or item.endswith('sword') or item.strip().endswith('dagger') or item.strip().endswith('axe') or item.strip().endswith('blade') or item.strip().endswith('baton') or item.strip().endswith('karambit') or item.strip().endswith('claw') or item.strip().endswith('balisong'):
      item_list2 = item.split(' ')
      for melee_item in item_list2:
        melee_list.append(melee_item)
    else:
      item_list3 = item.split(' ')
      for skin_item in item_list3:
        skin_list.append(skin_item)
  melee_key_list = jsonarray_to_list(get_melees())
  bundle_key_list = jsonarray_to_list(get_bundle())
  skins_key_list = jsonarray_to_list(get_skins())
  item_list_melee = common_member(melee_list,melee_key_list)
  item_list_skins = common_member(skin_list,skins_key_list)
  item_list_bundle = common_member(bundle_list,bundle_key_list)
  if not battlepass_count:
    count = 0
  else:
    count = battlepass_count

  print(item_list_skins)
  return extra_vp,item_list_melee,item_list_skins,item_list_bundle,count 

def calculate_total_vp(message):
  extra_vp,melee_set,skin_set,bundle_set,bp_count = get_list_of_items(message.replace('.',' '))
  melee_data = get_melees()
  skin_data = get_skins()
  bundle_data = get_bundle()
  melee_vp = 0
  skin_vp = 0
  bundle_vp = 0
  for melee in melee_set:
    for meleeobject in melee_data:
      try:
        melee_vp = melee_vp + int(meleeobject[melee])
      except:
        pass  
  print(melee_vp)
  for skin in skin_set:
    for skinobject in skin_data:
      try:
        print('skin_vp '+skinobject[skin])
        skin_vp = skin_vp + int(skinobject[skin])
      except:
        pass
  print(skin_vp)

  for bundle in bundle_set:
    for bundleobject in bundle_data:
      try:
        bundle_vp = bundle_vp + int(bundleobject[bundle])
      except:
        pass
  print(bundle_vp)
  bp_total = bp_count * 1000
  return extra_vp,melee_vp, skin_vp, bundle_vp, bp_total


def jsonarray_to_list(json_array):
  key_list = []
  for value in json_array:
    key_list.append(list(value.keys())[0])
  return key_list


def common_member(a,b): 
  common_itemlist = [] 
  for item_i in b:
    for item_j in a:
      if item_i == item_j:
        common_itemlist.append(item_i)
  return list(common_itemlist)
  
def embed_result_to_image(extra_vp,melee_vp, skin_vp, bundle_vp, bp_total,vp_spent,total_amount):
  img = Image.open("result.jpg")
  draw = ImageDraw.Draw(img)
  font_fname = 'FreeSansBold.ttf'
  font_size = 62
  large_font_size = 142
  large_font = ImageFont.truetype(font_fname,large_font_size)
  font = ImageFont.truetype(font_fname, font_size)
  draw.text((1777, 546),str(skin_vp)+' VP',(255,255,255),font=font)
  draw.text((2318, 546),str(bundle_vp)+' VP',(255,255,255),font=font)
  draw.text((2790, 546),str(melee_vp)+' VP',(255,255,255),font=font)
  draw.text((2010, 786),str(bp_total)+' VP',(255,255,255),font=font)
  draw.text((2603, 786),str(extra_vp)+' VP',(255,255,255),font=font)
  draw.text((1500, 1160),str(vp_spent)+' VP',(255,255,255),font=large_font)
  draw.text((1500, 1380),str(total_amount)+' Rs.',(255,255,255),font=large_font)
  img.save('sample-out.jpg')
  url = upload_img.upload_image('sample-out.jpg')
  print(url)
  return url








