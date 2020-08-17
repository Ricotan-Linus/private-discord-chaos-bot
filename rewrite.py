import discord
import json
from PIL import Image
import requests
import key
import os
import zbarlight
import argparse
import subprocess
import command
from bs4 import BeautifulSoup
import re
from pyzbar.pyzbar import decode

TOKEN = key.TOKEN
client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

def rep(c,s):
    d = str(c.pop(0)) + str(s.pop(0))
    d = re.sub(r"[./<=>\"]", "", d)
    d = re.sub(r'<a(.+)</a>', "", d)
    d = re.sub(r" ", "", d)
    d = d.replace('p', '').replace('classbold', '').replace('classtiny', '/').replace('Noissues', 'No issues').strip().strip()
    return d    

def get_shortenURL(longUrl):
    longUrl = longUrl
    access_token = key.access_token

    url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {"Authorization":'Bearer {}'.format(access_token),
            "Content-Type": "application/json",
            "Host": "api-ssl.bitly.com",
            "Accept":"application/json"
            }

    query = {
        "long_url":longUrl,
        "group_guid": 'Bjbb5t5fKqI',
        "domain": "bit.ly"
        }
    r = requests.post(url, json= query, headers= headers)
    print(r.status_code)
    r.json()
    try:
        r = r.json()['link']
    except KeyError:
        r = "error"
    return(r)

def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(r.content)

@client.event
async def on_message(message):
    if message.content.startswith("wakeup"):
        channel = client.get_channel(message.channel)
        id = "<@714406627603644489>"
        rico = "<@366844805470486528>"
        nu = int(150)
        for i in range(nu):
            await message.channel.send(id +" "+ rico + "起きて！！！")
    if message.content.startswith("廃人"):
        channel = client.get_channel(message.channel)
        res = requests.get('https://status.slack.com/')
        soup = BeautifulSoup(res.text, 'html.parser')
        c = soup.find_all('p',class_="bold")
        s = soup.find_all('p',class_="tiny")
        c = c[1:4]
        s = s[5:8]
        for i in range(3):
            d = rep(c,s)
            await message.channel.send(d)
    if message.content.startswith("ipcall"):
        channel = client.get_channel(message.channel)
        res = requests.get("http://inet-ip.info/ip")
        await message.channel.send(res.text)
    if message.content.startswith("プロセスを殺す"):
        channel = client.get_channel(message.channel)
        id = "<@366844805470486528>"
        await message.channel.send(id+"_"+"要請によりプロセスを緊急終了します")
        await message.channel.send("実行:"+"<@"+str(message.author.id)+">")
        os.kill(os.getpid(), 11)
    if message.content.startswith("フォースアゲイン"):
        channel = client.get_channel(message.channel)
        adminID = "<@366844805470486528>"
        SecondAdminID = "<@529644095027806208>"
        await message.channel.send(adminID+"\n"+SecondAdminID+"\n"+"再起動します")
        await message.channel.send("実行:"+"<@"+str(message.author.id)+">")
        os.system("reboot")
    if message.content.startswith("今日の大空お天気"):
        channel = client.get_channel(message.channel)
        soup = requests.get("https://www.aikatsu.com/onparade/")
        soup = BeautifulSoup(soup.text, 'html.parser')
        check = soup.find_all("div",class_='txt_detail-date')
        if check == []:
            soup = soup.find_all('dd',class_="txt_detail")
            soup = str(soup.pop(0))
            soup = soup.replace('<dd class="txt_detail">','').replace('</dd>','')
            print(soup)
            print(type(soup))
        else:
            check = soup.find_all("div",class_='txt_detail-date')
            soup = str(soup.pop(0))
            soup = re.sub(r'<br(.+)</p>', "", soup)
            soup = soup.replace('<p>', '')
            soup = soup.replace('</p>', '')
        await message.channel.send(soup)
    if message.content.startswith("金沢地方の遅れ"):
        channel = client.get_channel(message.channel)
        soup = requests.get("https://trafficinfo.westjr.co.jp/hokuriku.html")
        soup = BeautifulSoup(soup.text, 'html.parser')
        check = soup.find_all("p",class_='gaiyo')
        if check == []:
            soup = soup.find_all('strong')
            soup = str(soup.pop(0))
            soup = soup.replace('<strong>', '')
            soup = soup.replace('</strong>', '')
            await message.channel.send(soup)
        else:
            ls = soup.find_all('p',class_='gaiyo')
            while True:
                soup = ls.pop(0)
                soup = str(soup)
                soup = soup.replace('<p class="gaiyo">', '')
                soup = soup.replace('<br/>','')
                soup = soup.replace('</p>', '')
                await message.channel.send(soup)
                if ls == []:
                    break
    if message.content.startswith("近畿地方の遅れ"):
        channel = client.get_channel(message.channel)
        soup = requests.get("https://trafficinfo.westjr.co.jp/kinki.html")
        soup = BeautifulSoup(soup.text, 'html.parser')
        check = soup.find_all("p",class_='gaiyo')
        if check == []:
            soup = soup.find_all('strong')
            soup = str(soup.pop(0))
            soup = soup.replace('<strong>', '')
            soup = soup.replace('</strong>', '')
            await message.channel.send(soup)
        else:
            ls = soup.find_all('p',class_='gaiyo')
            while True:
                soup = ls.pop(0)
                soup = str(soup)
                soup = soup.replace('<p class="gaiyo">', '')
                soup = soup.replace('<br/>','')
                soup = soup.replace('</p>', '')
                await message.channel.send(soup)
                if ls == []:
                    break
    if message.content.startswith("プロセス把握"):
        channel =client.get_channel(message.channel)
        global response
        response = str(subprocess.check_output(['ps',"aux"]))
        print(response)
        response.replace(' ', '\n')
        response = response[:2000]
        await message.channel.send(response)
    if message.content.startswith("キモオタ"):
        channel =client.get_channel(message.channel)
        ID = "<@714406627603644489>"
        response = subprocess.check_output(['ojichat',"なぼ"]).decode(encoding='utf-8').rstrip()
        response = ID + response
        print(response)
        await message.channel.send(response)
    if not len(message.attachments)==0:
        RN = None
        channel = client.get_channel(message.channel)
        await message.channel.send('受け付けました')
        filename = message.attachments[0].filename
        download_img(message.attachments[0].url, filename)
        file_path = filename
        #try:
        read = decode(Image.open(file_path))
        #except OSError:
            #await message.channel.send('LINEのQRを送ろうとしていませんか？')
            #os.remove(filename)
        #finally:
            #pass
        path = read[0][0].decode('utf-8', 'ignore')
        print(path)
        print(type(path))
        if path is None:
            await message.channel.send("Error! QRコードが検出されませんでした。")
            os.remove(filename)
            return
        path = path.pop(0)
        path = path.decode('utf-8')
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
        print(path)
        if path == "error":
            await message.channel.send("Error! おそらくKyashなどのアプリ内でのみ使えるQRを送信しようとしていませんか？")
            os.remove(filename)
            path = card = r = None
            return
        else:
            await message.channel.send(RN)
            await message.channel.send(path)
            os.remove(filename)
            path = card = r = None

client.run(TOKEN)
