import subprocess
import discord
import os
import key
import socket
import datetime
import random

TOKEN = key.basedTOKEN
client = discord.Client()

@client.event
async def on_ready():
    print('WakeUp...')
    subprocess.Popen(["/Library/Frameworks/Python.framework/Versions/3.7/bin/python3","/Users/jr485/Aikatsu-QR-Multi-Post-Program/kick.py"])
    subprocess.Popen(["/Library/Frameworks/Python.framework/Versions/3.7/bin/python3","/Users/jr485/Aikatsu-QR-Multi-Post-Program/rewrite.py"])
    subprocess.Popen(["/Library/Frameworks/Python.framework/Versions/3.7/bin/python3","/Users/jr485/Aikatsu-QR-Multi-Post-Program/search.py"])
    subprocess.Popen(["/Library/Frameworks/Python.framework/Versions/3.7/bin/python3","/Users/jr485/Aikatsu-QR-Multi-Post-Program/kazune.py"])
    
@client.event
async def on_message(message):
    if "3407" in message.content:
            channel = client.get_channel(message.channel)
            await message.delete()
            await message.channel.send("!b "+message.author.mention)
    if "TTT" in message.content:
            channel = client.get_channel(message.channel)
            await message.delete()
            await message.channel.send("!b "+message.author.mention)
    if message.content.startswith('whoami'):
        channel = client.get_channel(message.channel)
        llip = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
        await message.channel.send("私は"+socket.gethostname()+"だよっ☆"+"\n"+"ローカルipは"+llip+"だよっ☆")
    if 'kickup' in message.content:
        channel = client.get_channel(message.channel)
        subprocess.Popen(["/Library/Frameworks/Python.framework/Versions/3.7/bin/python3","/Users/jr485/Aikatsu-QR-Multi-Post-Program/kick.py"])
        await message.channel.send("<@744874026966581380>"+"を叩き起こしました")
    if 'postup' in message.content:
        channel = client.get_channel(message.channel)
        subprocess.Popen(["/Library/Frameworks/Python.framework/Versions/3.7/bin/python3","/Users/jr485/Aikatsu-QR-Multi-Post-Program/rewrite.py"])
        await message.channel.send("<@673755083061723136>"+"を叩き起こしました")
    if 'kznboot' in message.content:
        subprocess.Popen(["/Library/Frameworks/Python.framework/Versions/3.7/bin/python3","/Users/jr485/Aikatsu-QR-Multi-Post-Program/kazune.py"])
        channel = client.get_channel(message.channel)
        await message.channel.send("<@780775643276771348>"+"を叩き起こしました")
    if 'searchawake' in message.content:
        subprocess.Popen(["/Library/Frameworks/Python.framework/Versions/3.7/bin/python3","/Users/jr485/Aikatsu-QR-Multi-Post-Program/search.py"])
        channel = client.get_channel(message.channel)
        await message.channel.send("<@779235375172026389>"+"を叩き起こしました")     
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
