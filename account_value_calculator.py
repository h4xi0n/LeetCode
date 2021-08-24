import json

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
    if item.endswith('battlepass') or item.endswith('bp'):
      battlepass_count = [int(s) for s in item.split() if s.isdigit()]
    elif item.endswith('vp'):
      extra_vp = [int(s) for s in item.split() if s.isdigit()][0]
    elif item.endswith('bundle'):
      item_list1 = item.split(' ')
      for bundle_item in item_list1:
        bundle_list.append(bundle_item)
    elif item.endswith('melee') or item.endswith('knife') or item.endswith('sword') or item.endswith('dagger') or item.endswith('axe'):
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
    count = battlepass_count[0]
  return extra_vp,item_list_melee,item_list_skins,item_list_bundle,count 

def calculate_total_vp(message):
  extra_vp,melee_set,skin_set,bundle_set,bp_count = get_list_of_items(message.replace('.',''))
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
  








