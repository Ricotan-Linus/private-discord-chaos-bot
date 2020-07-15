import requests
from bs4 import BeautifulSoup
import re
import discord
import key

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

@client.event
async def on_message(message):
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
                    
client.run(TOKEN)