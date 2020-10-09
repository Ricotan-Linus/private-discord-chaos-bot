import subprocess
import discord
import os
import key
import socket
import datetime

TOKEN = key.basedTOKEN
client = discord.Client()

@client.event
async def on_ready():
    print('WakeUp...')
    subprocess.Popen(["sudo","/Library/Frameworks/Python.framework/Versions/3.7/bin/python3","kick.py"])
    subprocess.Popen(["sudo","/Library/Frameworks/Python.framework/Versions/3.7/bin/python3","rewrite.py"])
    
@client.event
async def on_message(message):
    if "なぼ" in message.content:
        channel = client.get_channel(message.channel)
        await message.delete()
        await message.channel.send("表現規制フィルターを発動しました")
        with open("log.txt", mode='a') as f:
            dt_now = datetime.datetime.now()
            f.write("["+str(dt_now)+"]"+"\n"+str(message.author)+"が"+"なぼ"+"で引っかかりました"+"\n"+"本文:"+str(message.content)+"\n")
            print("ログ書き込み")
        f.close()
        return
    if "な ぼ" in message.content:
        channel = client.get_channel(message.channel)
        await message.delete()
        await message.channel.send("表現規制フィルターを発動しました")
        with open("log.txt", mode='a') as f:
            f.write("["+str(dt_now)+"]"+"\n"+str(message.author)+"が"+"な ぼ"+"で引っかかりました"+"\n"+"本文:"+str(message.content)+"\n")
            print("ログ書き込み")
        f.close()
        return
    if "な、ぼ" in message.content:
        channel = client.get_channel(message.channel)
        await message.delete()
        await message.channel.send("表現規制フィルターを発動しました")
        with open("log.txt", mode='a') as f:
            f.write("["+str(dt_now)+"]"+"\n"+str(message.author)+"が"+"な、ぼ"+"で引っかかりました"+"\n"+"本文:"+str(message.content)+"\n")
            print("ログ書き込み")
        f.close()
        return
    if "な/ぼ" in message.content:
        channel = client.get_channel(message.channel)
        await message.delete()
        await message.channel.send("表現規制フィルターを発動しました")
        with open("log.txt", mode='a') as f:
            f.write("["+str(dt_now)+"]"+"\n"+str(message.author)+"が"+"な/ぼ"+"で引っかかりました"+"\n"+"本文:"+str(message.content)+"\n")
            print("ログ書き込み")
        f.close()
        return
    if "な|ぼ" in message.content:
        channel = client.get_channel(message.channel)
        await message.delete()
        await message.channel.send("表現規制フィルターを発動しました")
        with open("log.txt", mode='a') as f:
            f.write("["+str(dt_now)+"]"+"\n"+str(message.author)+"が"+"な|ぼ"+"で引っかかりました"+"\n"+"本文:"+str(message.content)+"\n")
            print("ログ書き込み")
        f.close()
        return
    if "ナボ" in message.content:
        channel = client.get_channel(message.channel)
        await message.delete()
        await message.channel.send("表現規制フィルターを発動しました")
        with open("log.txt", mode='a') as f:
            f.write("["+str(dt_now)+"]"+"\n"+str(message.author)+"が"+"ナボ"+"で引っかかりました"+"\n"+"本文:"+str(message.content)+"\n")
            print("ログ書き込み")
        f.close()
        return
    if "3407" in message.content:
            channel = client.get_channel(message.channel)
            await message.channel.send("!b "+message.author.mention)
    if message.content.startswith('whoami'):
        channel = client.get_channel(message.channel)
        llip = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
        await message.channel.send("私は"+socket.gethostname()+"だよっ☆"+"\n"+"ローカルipは"+llip+"だよっ☆")
    if message.content.startswith('kickup'):
        channel = client.get_channel(message.channel)
        subprocess.Popen(["python3","kick.py"])
        await message.channel.send("<@744874026966581380>"+"を叩き起こしました")
    if message.content.startswith('postup'):
        channel = client.get_channel(message.channel)
        subprocess.Popen(["python3","rewrite.py"])
        await message.channel.send("<@673755083061723136>"+"を叩き起こしました")
    if message.content.startswith('セグメントフォール'):
        if "モデレーターさん" in [users_role.name for users_role in message.author.roles]:
                id = "<@366844805470486528>"
                await message.channel.send(id+"宛。"+"緊急終了実行。")
                await message.channel.send("実行:"+"<@"+str(message.author.id)+">")
                await client.logout()
                os.kill(os.getpid(), 11)
    
client.run(TOKEN)
