import discord
import json
from PIL import Image
from pyzbar import pyzbar
from pyzbar.pyzbar import decode
import requests
import key
from bs4 import BeautifulSoup

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
        RN = None
        channel = client.get_channel(message.channel)
        await message.channel.send('受け付けました')
        print(type(message))
        print(type(message.attachments))
        print(message.attachments[0])
        filename = message.attachments[0].filename
        download_img(message.attachments[0].url, filename)
        path = filename
        path = decode(Image.open(path))
        path = path[0][0].decode('utf-8', 'ignore')
        print(path)
        if "http://dcd.sc/n2" in path:
            target_url = path
            r = requests.get(target_url) 
            soup = BeautifulSoup(r.text, 'lxml')
            try:
                NR = soup.find("dd", class_="cardNum").get_text()
                RR = soup.find("dd", class_="cardName").get_text()
                RN = NR + "_" + RR
                print(RN)
            except AttributeError:
                RN = "カード名取得失敗です。学生証を読み込んだ事またはリダイレクトの設定間違えだと思われます。"
        elif "http://dcd.sc/j2" in path:
            target_url = path
            r = requests.get(target_url) 
            soup = BeautifulSoup(r.text, 'lxml')
            try:
                NR = soup.find("div", class_="dress-detail-title clearfix").get_text()
                print(NR)
                RN = NR
                print(RN)
            except AttributeError:
                RN = "カード名取得失敗です。学生証を読み込んだ事またはリダイレクトの設定間違えだと思われます。"
        elif "http://dcd.sc/n3" in path or "http://dcd.sc/n1" in path:
            NR = "学生証です。"
            print(NR)
            RN = NR
        elif "http://dcd.sc/n0" in path:
            NR = "アイドルカードまたはフルコーデカードです。"
            print(NR)
            RN = NR
        path = get_shortenURL(path)
        try:
            card = path['data']['url']
        except TypeError:
            RN = "旧カツカードまたは読み込めない形式のカードです。"
            card = "対応カードはgithubのreadmeをご覧ください。"
        await message.channel.send(RN)
        await message.channel.send(card)
        path = card = None

client.run(TOKEN)