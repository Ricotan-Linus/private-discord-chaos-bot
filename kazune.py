from glob import glob
import subprocess
import discord
import os
import key
import socket
import datetime
import random
    
TOKEN = key.kzn_token
client = discord.Client()
l = []

@client.event
async def on_ready():
    print('WakeUp...')
    for file in glob("/Users/jr485/Aikatsu-QR-Multi-Post-Program/kazune_img"+ '/*.jpg'):
        global l
        l.append(file)
    
@client.event
async def on_message(message):
    if message.content.startswith('whoami'):
        channel = client.get_channel(message.channel)
        llip = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
        await message.channel.send("私は"+socket.gethostname()+"だよっ☆"+"\n"+"ローカルipは"+llip+"だよっ☆")
    if message.content.startswith("kazune"):
        channel = message.channel
        a = random.choice(l)
        print(a)
        b = l.index(a)+1
        with open(a, 'rb') as fp:
            await channel.send(file=discord.File(fp, str(b)+'.jpg'))
            await message.channel.send("これは"+str(b)+"番目の画像です。")
    if message.content.startswith('セグメントフォール'):
        if "モデレーターさん" in [users_role.name for users_role in message.author.roles]:
                id = "<@366844805470486528>"
                await message.channel.send(id+"宛。"+"緊急終了実行。")
                await message.channel.send("実行:"+"<@"+str(message.author.id)+">")
                await client.logout()
                os.kill(os.getpid(), 11)
    if message.content.startswith('オールデリート'):
            if "モデレーターさん" in [users_role.name for users_role in message.author.roles]:
                id = "<@366844805470486528>"
                await message.channel.send(id+"宛。"+"緊急終了実行。")
                await message.channel.send("実行:"+"<@"+str(message.author.id)+">")
                await client.logout()
                __import__("ctypes").string_at(0)
    if message.content.startswith('pid'):
        channel = client.get_channel(message.channel)
        await message.channel.send(pid)
    if message.content.startswith('!kill'):
        if "モデレーターさん" in [users_role.name for users_role in message.author.roles]:
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
        
pid = random.randrange(10001)
client.run(TOKEN)
