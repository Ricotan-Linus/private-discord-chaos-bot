# -*- coding: UTF-8 -*-

import os
import requests
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
import slack

# SLACK_BOT_TOKEN = key.SLACK_BOT_TOKEN


def SearchImage():
    homeDir = expanduser('~')
    imageDir = homeDir + '\\Pictures\\Camera Roll'
    imageList = os.listdir(imageDir)
    return (imageDir + '\\' + imageList[-1])


def QRreade(image):
    readResult = decode(Image.open(image))
    if (readResult != []):
        return readResult
    else:
        print('QRコードを検出できませんでした')
        exit()


def get_shortenURL(longUrl):
    url = 'https://api-ssl.bitly.com/v3/shorten'
    access_token = key.access_token
    query = {
        'access_token': access_token,
        'longurl': longUrl,
    }
    r = requests.get(url, params=query).json()
    return r


def post(card):
    slackch = key.slackch

    client = slack.WebClient(token=SLACK_BOT_TOKEN)
    response = client.chat_postMessage(channel=slackch, text=card)



def main():
    print(
        """アイカツQRコードSlack送信システム
該当の画像があるパスを入れてください
QRを読み取る場合はQR-Readと入れてください
カメラが起動します
終了する場合はexitまたはCtrl+Dでお願いします
URLのサポートは打ち切りました。"""
    )

    while True:
        try:
            path = input()
        except UnicodeDecodeError:
            print("ファジングしようとするなあ！！！！！！！！！！！！！！！！")
            sys.exit()

        path = path.strip()

        if "exit" in path:
            exit()

        domain = pathlib.Path(path)
        domain = domain.suffix.lower()
        if_suffix = ['.jpg', '.png', '.bmp', '.tif', '.jpeg']
        if domain in if_suffix:
            pass
        elif "QR" in path:
            pass
        else:
            print("これ画像じゃないですよね...")
            print("再実行しますか？[Y/N]")
            try:
                retry = input().strip().lower()
            except UnicodeDecodeError:
                print("ファジングしようとするなあ！！！！！！！！！！！！！！！！")
                sys.exit()
            except EOFError:
                print("不正な文字列を入れてませんか？？？")
                sys.exit()
            if retry == 'y':
                continue
            elif retry == 'n':
                break
            else:
                print("リトライしてください")
                continue

        if "QR" in path:
            window_name = "main"
            cap = cv2.VideoCapture(0)
            cap.set(3, 1280)
            cap.set(4, 720)
            cap.set(5, 15)
            cv2.namedWindow(window_name)

            while True:
                ret, flame = cap.read()
                cv2.imshow(window_name, flame)
                tresh = 100
                max_pixel = 255
                ret, flame = cv2.threshold(flame, tresh, max_pixel, cv2.THRESH_BINARY)
                qr_result = pyzbar.decode(flame)
                if qr_result != []:
                    path = qr_result[0][0].decode('utf-8', 'ignore')
                    print(path)
                    if "http://dcd.sc/" not in path and "http://aikatsu.com/qr/id=" in path and "AK" in path:
                        print("アイカツ以外のカードは読み込めません。悪しからず。")
                        sys.exit()
                    break
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        if "http://aikatsu.com/qr/id=" in path:
            print("旧カツのカードは対応していません。別のカードを読み込んでください。")
            print("該当の画像を入れてください")
            print("終了する場合はexitまたはCtrl+Dでお願いします")
            path = None
            continue

        if "AK" in path:
            print("旧カツのカードは対応していません。別のカードを読み込んでください。")
            print("該当の画像を入れてください")
            print("終了する場合はexitまたはCtrl+Dでお願いします")
            path = None
            continue

        cv2.destroyAllWindows()

        if "http://dcd.sc/" not in path:
            try:
                read = decode(Image.open(path))
            except FileNotFoundError:
                print("本当にそこにありますか？？？")
                print("再実行しますか？[Y/N]")
                try:
                    retry = input()
                except EOFError:
                    print("不正な文字列を入れてませんか？？？")
                    sys.exit()
                except UnicodeDecodeError:
                    print("ファジングしようとするなあ！！！！！！！！！！！！！！！！")
                    sys.exit()
                if retry.lower() in y:
                    continue
                elif retry.lower() in n:
                    break
                else:
                    print("リトライしてください")
                    continue
            except OSError:
                print("画像ファイルに見せかけた不正なファイルを読み込ませないでください")
                print("強制終了します")
                sys.exit()

            path = read[0][0].decode('utf-8', 'ignore')

        path = get_shortenURL(path)

        print(path)

        try:
            card = path['data']['url']
        except TypeError:
            print("旧カツカードまたは読み込めない形式のカードです、別のカードを読み込んでください。")
            print("該当の画像を入れてください")
            print("終了する場合はexitまたはCtrl+Dでお願いします")
            path = None
            continue

        post(card)

        card = image = path = None

        print("該当の画像を入れてください")
        print("終了する場合はexitまたはCtrl+Dでお願いします")

if __name__ == '__main__':
    main()
