#!/usr/bin/env python
# -*- coding: utf-8 -
import subprocess
import discord
import os
import socket
import datetime
import random
import requests
from bs4 import BeautifulSoup
import key

TOKEN = key.search_token
client = discord.Client()

CN = []#オンパレカードネーム用。
CU = []#オンパレカードナンバー用。
CR = []#オンパレカード用。
CP = []#リサルト
JN = []#カードネーム
JU = []#カードナンバー
JR = []#カード
JP = []#リザ
RCN = []#統合用


res = requests.get('https://www.aikatsu.com/onparade/cardlist/index.php?search=true')
soup = BeautifulSoup(res.text, 'html.parser')

for l in soup.find_all("dd", class_="cardName"):
    print(l.text)
    CN.append(l.text)
    
for l in soup.find_all("dd", class_="cardNum"):
    print(l.text)
    CU.append(l.text)
    
print(CU)
print(CN)

while True:
    a = CU.pop(0)
    b = CN.pop(0)
    CR.append(a+" "+b)
    if CU == [] and CN == []:
        break
    print(CR)
    
res = requests.get('https://www.aikatsu.com/friends/cardlist/index.php?search=true')
soup = BeautifulSoup(res.text, 'html.parser')

for l in soup.find_all("dd", class_="cardName"):
    print(l.text)
    JN.append(l.text)
    
for l in soup.find_all("dd", class_="cardNum"):
    print(l.text)
    JU.append(l.text)
    
print(JN)
print(JU)

while True:
    a = JU.pop(0)
    b = JN.pop(0)
    JR.append(a+" "+b)
    if JU == [] and JN == []:
        break
    print(JR)
    
RCN = CR + JR

@client.event
async def on_ready():
    print('WakeUp...')

@client.event
async def on_message(message):
    if message.content.startswith('!s'):
        global RCN
        global CN
        global CU
        global CP
        if message.author.bot == True:
            return
        channel = client.get_channel(message.channel)
        req = message.content[3:]
        
        for CCR in RCN:
            if req in CCR:
                try:
                    CP.append(CCR)
                except AttributeError:
                    CCR = []
                    CP = []
                    return
            else:
                pass
        CP = '\n'.join(CP)
        print(type(CP))
        print(len(CP))
        if len(CP) == 0:
            CCR = []
            CP = []
            await message.channel.send("該当するカードがありません。")
            return
        await message.channel.send(CP[:1999])
        CP = []
    if message.content.startswith('オールデリート'):
        if "モデレーターさん" in [users_role.name for users_role in message.author.roles]:
            id = "<@366844805470486528>"
            await message.channel.send(id+"宛。"+"緊急終了実行。")
            await message.channel.send("実行:"+"<@"+str(message.author.id)+">")
            await client.logout()
            os.kill(os.getpid(), 11)
    if message.content.startswith('pid'):
        channel = client.get_channel(message.channel)
        await message.channel.send(pid)
    if message.content.startswith('!kill'):
        if str(pid) in message.content:
            if message.author.bot:
                return
            else:
                id = "<@366844805470486528>"
                await message.channel.send(id+"宛。"+"緊急終了実行。")
                await message.channel.send("実行:"+"<@"+str(message.author.id)+">")
                await client.logout()
                os.kill(os.getpid(), 11)
        else:
            return
    if message.content.startswith('捜索終了'):
        if "モデレーターさん" not in [users_role.name for users_role in message.author.roles]:
            return
        channel = client.get_channel(message.channel)
        await message.channel.send("検索終了します。")
        await message.channel.send("実行:"+"<@"+str(message.author.id)+">")
        await client.logout()
        os.kill(os.getpid(), 11)
    if message.content.startswith('whoami'):
        channel = client.get_channel(message.channel)
        llip = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
        await message.channel.send("このbotが動いているサーバーは"+socket.gethostname()+"です。"+"\n"+"ローカルipは"+llip+"となります。")

pid = random.randrange(10001)
client.run(TOKEN)