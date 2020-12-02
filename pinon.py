import discord
import key
import socket
import os

TOKEN = key.pinon_TOKEN
intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.content.startswith('ライブ終了'):
        channel = client.get_channel(message.channel)
        await message.channel.send("ぴのんのライブ見に来てくれてありがとっぴ☆")
        await message.channel.send("実行:"+"<@"+str(message.author.id)+">")
        await client.logout()
        os.kill(os.getpid(), 11)
    if message.content.startswith('whoami'):
        channel = client.get_channel(message.channel)
        llip = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
        await message.channel.send("このbotが動いているサーバーは"+socket.gethostname()+"ぴっぴ☆"+"\n"+"ローカルipは"+llip+"ぴっぴ☆")
    if message.content.startswith('!k'):
        if "モデレーターさん" in [users_role.name for users_role in message.author.roles]:
            channel = message.channel
            print(type(channel))
            KickUser = message.mentions
            print(KickUser)
            l_length = len(KickUser)
            for i in range(l_length):
                KickUserDate = str(KickUser.pop(0))
                KickUserDate = KickUserDate[:-5]
                print(KickUserDate)
                user = discord.utils.get(message.guild.members, name=KickUserDate)
                await user.kick()
                await message.channel.send(file=discord.File('power.mov'))
                await message.channel.send(KickUserDate+"を蹴り飛ばしました")
        elif "りこたんの右腕" in [users_role.name for users_role in message.author.roles]:
            channel = client.get_channel(message.channel)
            KickUser = message.mentions
            print(KickUser)
            l_length = len(KickUser)
            for i in range(l_length):
                KickUserDate = str(KickUser.pop(0))
                KickUserDate = KickUserDate[:-5]
                print(KickUserDate)
                user = discord.utils.get(message.guild.members, name=KickUserDate)
                await user.kick()
                await message.channel.send(file=discord.File('power.mov'))
                await message.channel.send(KickUserDate+"を蹴り飛ばしました")
        else:
            return
    if message.content.startswith('!b'):
        if "モデレーターさん" in [users_role.name for users_role in message.author.roles]:
            channel = client.get_channel(message.channel)
            BanUser = message.mentions
            print(BanUser)
            for Busu in BanUser:
                Busu = Busu[:-5]
                print(Busu)
                user = discord.utils.get(message.guild.members, name=Busu)
                await ban(user,delete_message_days=0)
                await message.channel.send(file=discord.File('power.mov'))
                await message.channel.send(BanUserDate+"を潰しました")
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
                await ban(user,reason="bot order",delete_message_days=0)
                await message.channel.send(file=discord.File('power.mov'))
                await message.channel.send(BanUserDate+"を潰しました")
        else:
            return
client.run(TOKEN)
