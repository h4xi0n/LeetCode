import os
import pyimgur

client_id = os.environ['CLIENT_ID']

client_secret = os.environ['AUTH_TOKEN']

def upload_image(image_path):
  im = pyimgur.Imgur(client_id,client_secret)
  uploaded_image = im.upload_image(path=image_path, title="Gaming Project")
  print(uploaded_image.link)
  return uploaded_image.link