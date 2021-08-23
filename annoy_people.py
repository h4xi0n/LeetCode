import requests
import json
import utilities
#Pass Member/User.mention object
def get_compliment(user):
  response = requests.get('https://complimentr.com/api')
  json_data = json.loads(response.text)
  compliment = json_data['compliment']
  if 'you are' in compliment:
    print('you are')
    compliment = utilities.replace(compliment,'you are',user+' is')
  if 'you' in compliment:
    print('you')
    compliment = utilities.replace(compliment,'you',user)
  return compliment

def get_insult(user):
  response = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
  json_data = json.loads(response.text)
  insult = json_data['insult']
  return 'Hey '+user+', '+insult


