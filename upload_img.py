import os
import pyimgur
import requests
bit_ly_token = os.environ['BIT_LY_TOKEN']
bit_ly_username = os.environ['BIT_LY_USERNAME']
client_id = os.environ['CLIENT_ID']

client_secret = os.environ['AUTH_TOKEN']

def upload_image(image_path):
  im = pyimgur.Imgur(client_id,client_secret)
  uploaded_image = im.upload_image(path=image_path, title="Gaming Project")
  print(uploaded_image.link)
  return uploaded_image.link


def shorten(uri):
    query_params = {
        'access_token': bit_ly_token,
        'longUrl': uri
    }

    endpoint = 'https://api-ssl.bitly.com/v3/shorten'
    response = requests.get(endpoint, params=query_params, verify=False)

    data = response.json()


    if not data['status_code'] == 200:
        print(response.url)

    return data['data']['url']