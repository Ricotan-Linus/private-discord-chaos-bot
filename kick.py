import discord
import subprocess
import key
import socket
import os

TOKEN = key.CentralTOKEN
client = discord.Client()

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
    #if message.content.startswith("!cwk"):
        #channel = client.get_channel(message.channel)
        #global number
        #try:
            #message.content = int(message.content[4:])
        #except ValueError:
            #await message.channel.send("数値ではないので回数変更できませんっ！")
            #return
        #if message.content >= int(1001):
            #await message.channel.send("1000以上の数値をやらせようとしないでくださいっ！")
            #return
        #else:
            #number = message.content
            #await message.channel.send("叩き起こすメンションの回数を"+str(number)+"に変更しましたっ！")
            #return
    #if message.content.startswith("!awk"):
        #if "モデレーターさん" in [users_role.name for users_role in message.author.roles]:
            #conf_on()
            #await message.channel.send("Wakeup可能ですっ！")
    #if message.content.startswith("!dwk"):
        #if "モデレーターさん" in [users_role.name for users_role in message.author.roles]:
            #conf_off()
            #await message.channel.send("Wakeup無効ですっ！")
    #if message.content.startswith("!whichwk"):
        #if "on" in wu:
            #await message.channel.send("Wakeup可能ですっ！")
        #else:
            #await message.channel.send("Wakeup無効ですっ！")
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
    #if message.content.startswith("!ask"):
        #channel = client.get_channel(message.channel)
        #key.sck = "on"
        #await message.channel.send("なぼーんを発言禁止にしました")
    #if message.content.startswith("!dsk"):
        #channel = client.get_channel(message.channel)
        #key.sck = "off"
        #await message.channel.send("なぼーんの発言禁止を解除しました")
    #if str(message.author) == "なぼーん#2696":
        #if key.sck == "on":
                #await message.delete()
                #await message.channel.send("!k "+message.author.mention)
        #else:
            #pass
    if message.content.startswith('!k'):
        if "モデレーターさん" or "りこたんの右腕" in [users_role.name for users_role in message.author.roles]:
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
                await message.channel.send("https://cdn.discordapp.com/attachments/734039650330607657/745431796098793519/c4333207179bc37d.mov")
                await message.channel.send(KickUserDate+"を蹴り飛ばしました")
    if message.content.startswith('!b'):
        if "モデレーターさん" or "りこたんの右腕" in [users_role.name for users_role in message.author.roles]:
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
    #if message.content.startswith("wakeup"):
        #channel = client.get_channel(message.channel)
        #id = "<@714406627603644489>"
        #rico = "<@366844805470486528>"
        #for i in range(number):
            #await message.channel.send(id +" "+ rico + "起きて！！！")

abc()
client.run(TOKEN)
