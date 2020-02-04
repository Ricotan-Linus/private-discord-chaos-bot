# -*- coding: UTF-8 -*-
import os
import json
import time
import sys
import pathlib
import cv2
import key
import path
from PIL import Image
from pyzbar import pyzbar
from pyzbar.pyzbar import decode
import requests
from bs4 import BeautifulSoup

SLACK_BOT_TOKEN = key.SLACK_BOT_TOKEN

def get_shortenURL(longUrl):
    url = 'https://api-ssl.bitly.com/v3/shorten'
    access_token = key.access_token
    query = {
        'access_token': access_token,
        'longurl': longUrl,
    }
    r = requests.get(url, params=query).json()
    return r

def main():
    TOKEN = key.TOKEN
        
    client = discord.Client()
    
    client.run(TOKEN)
        
    print(
        """アイカツQRコード読み取り/Slack送信システム
該当の画像があるパスを入れてください
QRを読み取る場合はQRと入れてください
終了する場合はexitまたはCtrl+Dでお願いします"""
    )

    while True:
        path = 

        if "http://aikatsu.com/qr/id=" in path or "AK" in path and "http://dcd.sc/" not in path:
            print(
                """旧カツのカードは対応していません。
該当の画像を入れてください
終了する場合はexitまたはCtrl+Dでお願いします"""
            )
            path = None
            continue

            read = decode(Image.open(path))

            path = read[0][0].decode('utf-8', 'ignore')
            
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
                    print("カード名取得失敗です。学生証を読み込んだ事またはリダイレクトの設定間違えだと思われます。")
                    RN = "カード名取得失敗です。学生証を読み込んだ事またはリダイレクトの設定間違えだと思われます。"
                    pass
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
                    print("カード名取得失敗です。学生証を読み込んだ事またはリダイレクトの設定間違えだと思われます。")
                    RN = "カード名取得失敗です。学生証を読み込んだ事またはリダイレクトの設定間違えだと思われます。"
                    pass
                else:
                    pass
            elif "http://dcd.sc/n3" in path or "http://dcd.sc/n1" in path:
                NR = "学生証です。"
                print(NR)
                RN = NR
            elif "http://dcd.sc/n0" in path:
                NR = "アイドルカードです。"
                print(NR)
                RN = NR

        path = get_shortenURL(path)

        print(path)

        try:
            card = path['data']['url']
        except TypeError:
            print("旧カツカードまたは読み込めない形式のカードです。")
            print("該当の画像を入れてください")
            print("終了する場合はexitまたはCtrl+Dでお願いします")
            path = None
            continue
        
        card = RN + "\n" + card

        card = image = path = RN = RR = NR = None

        print("該当の画像を入れてください")
        print("終了する場合はexitまたはCtrl+Dでお願いします")


if __name__ == '__main__':
    main()
