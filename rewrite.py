import discord
import json
from PIL import Image
from pyzbar import pyzbar
from pyzbar.pyzbar import decode
import requests
import key

TOKEN = key.TOKEN
client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

def get_shortenURL(longUrl):
    url = 'https://api-ssl.bitly.com/v3/shorten'
    access_token = key.access_token
    query = {
        'access_token': access_token,
        'longurl': longUrl,
    }
    r = requests.get(url, params=query).json()
    return r

def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(r.content)

@client.event
async def on_message(message):
    if str(client.user.id) in message.content:
        print("True")
        if message.content.startswith('/pic'):
            await client.send_message(channel, '画像確認')
            filename = str(message.attachments[0]['filename'])
            download_img(message.attachments[0]['url'], "image.png")
            await client.send_message(channel, '画像確認')
            path = "image.png"
            path = decode(Image.open(path))
            path = path[0][0].decode('utf-8', 'ignore')
            print(path)
            path = get_shortenURL(path)
            client.send_message(channel, path)
            path = None

client.run(TOKEN)