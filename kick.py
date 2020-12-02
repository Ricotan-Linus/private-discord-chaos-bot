import discord
import subprocess
import key
import socket
import os
import random

intents = discord.Intents.all()
intents.members = True

TOKEN = key.CentralTOKEN
client = discord.Client(intents=intents)

def abc():
    global number
    number = int(150)

#wakeup CONFIG
wu = "on"

def conf_on():
    global wu
    wu = "on"
    
def conf_off():
    global wu
    wu = "off"
    
@client.event
async def on_message(message):
    if message.content.startswith('フォースクラッシュ'):
        channel = client.get_channel(message.channel)
        id = "<@366844805470486528>"
        await message.channel.send(id+"へ！"+"プロセス止めちゃうね！")
        await message.channel.send("実行:"+"<@"+str(message.author.id)+">")
        await client.logout()
        os.kill(os.getpid(), 11)
    if message.content.startswith('whoami'):
        channel = client.get_channel(message.channel)
        llip = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
        await message.channel.send("私は"+socket.gethostname()+"だよっ☆"+"\n"+"ローカルipは"+llip+"だよっ☆")
    if message.content.startswith('!k'):
        if "モデレーターさん" in [users_role.name for users_role in message.author.roles]:
            channel = client.get_channel(message.channel)
            KickUser = message.mentions
            print(KickUser)
            l_length = len(KickUser)
            for i in range(l_length):
                KickUserDate = str(KickUser.pop(0))
                print(KickUserDate)
                KickUserDate = KickUserDate[:-5]
                print(KickUserDate)
                user = discord.utils.get(message.guild.members, name=str(KickUserDate))
                print(user)
                await user.kick()
                await message.channel.send("https://cdn.discordapp.com/attachments/734039650330607657/745431796098793519/c4333207179bc37d.mov")
                await message.channel.send(KickUserDate+"を蹴り飛ばしました")
                dm = await user.create_dm()
                try:
                    await dm.send("あなたはKickされました。下の招待リンクからどうぞ。"+"\n"+"discord.gg/dkFmdVr")
                except discord.errors.Forbidden:
                    pass
        elif "りこたんの右腕" in [users_role.name for users_role in message.author.roles]:
            channel = client.get_channel(message.channel)
            KickUser = message.mentions
            print(KickUser)
            l_length = len(KickUser)
            for i in range(l_length):
                KickUserDate = str(KickUser.pop(0))
                print(KickUserDate)
                user = discord.utils.get(message.guild.members, name=str(KickUserDate))
                await user.kick()
                await message.channel.send("https://cdn.discordapp.com/attachments/734039650330607657/745431796098793519/c4333207179bc37d.mov")
                await message.channel.send(KickUserDate+"を蹴り飛ばしました")
                dm = await user.create_dm()
                try:
                    await dm.send("あなたはKickされました。下の招待リンクからどうぞ。"+"\n"+"discord.gg/dkFmdVr")
                except discord.errors.Forbidden:
                    pass
        else:
            return
    if message.content.startswith('!b'):
        if "モデレーターさん" in [users_role.name for users_role in message.author.roles]:
            channel = client.get_channel(message.channel)
            BanUser = message.mentions
            print(BanUser)
            l_length = len(BanUser)
            for i in range(l_length):
                BanUserDate = str(BanUser.pop(0))
                BanUserDate = BanUserDate[:-5]
                print(BanUserDate)
                user = discord.utils.get(message.guild.members, name=BanUserDate)
                await user.ban()
                await message.channel.send("https://cdn.discordapp.com/attachments/734039650330607657/745431796098793519/c4333207179bc37d.mov")
                await message.channel.send(BanUserDate+"を潰しました")
                dm = await user.create_dm()
                try:
                    await dm.send("あなたはBANされました。概ね24時間以内に解除しますのでしばらくお待ちください。"+"\n"+"discord.gg/dkFmdVr")
                except discord.errors.Forbidden:
                    pass
        else:
            return
        elif "りこたんの右腕" in [users_role.name for users_role in message.author.roles]:
            channel = client.get_channel(message.channel)
            BanUser = message.mentions
            print(BanUser)
            l_length = len(BanUser)
            for i in range(l_length):
                BanUserDate = str(BanUser.pop(0))
                BanUserDate = BanUserDate[:-5]
                print(BanUserDate)
                user = discord.utils.get(message.guild.members, name=BanUserDate)
                await user.ban(reason="bot order")
                await message.channel.send("https://cdn.discordapp.com/attachments/734039650330607657/745431796098793519/c4333207179bc37d.mov")
                await message.channel.send(BanUserDate+"を潰しました")
                dm = await user.create_dm()
                try:
                    await dm.send("あなたはBANされました。概ね24時間以内に解除しますのでしばらくお待ちください。"+"\n"+"discord.gg/dkFmdVr")
                except discord.errors.Forbidden:
                    pass
        else:
            return
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
        
pid = random.randrange(10001)
client.run(TOKEN)
