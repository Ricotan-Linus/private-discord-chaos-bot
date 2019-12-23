# -*- coding: UTF-8 -*-

import os
import json
import time
import sys
import pathlib

import cv2
import key
import path  # これなんだ?
from PIL import Image
from pyzbar import pyzbar
from pyzbar.pyzbar import decode
import requests
import slack

SLACK_BOT_TOKEN = key.SLACK_BOT_TOKEN


def SearchImage():
    homeDir = expanduser('~')  # これなに?
    imageDir = pathlib.Path(homeDir) / "Pictures"/"Camera Roll"
    imageList = os.listdir(imageDir)  # pathlibでたぶん同じのあるけど、とりあえずそのままに
    out_path =os.path.join(imageDir,imageList[-1])  # strに変換するのめんどいのでos.pathで
    return (out_path)


def QRreader(image):
    readResult = decode(Image.open(image))
    if len(readResult) != 0:  # 配列が空でなかったら
        return readResult
    else:
        print('QRコードを検出できませんでした')
        sys.exit(0)


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


def get_path():
    while True:
        try:
            path = input()
        except UnicodeDecodeError:
            print("ファジングしようとするなあ！！！！！！！！！！！！！！！！")
            sys.exit(1)  # 異常終了時は1

        path = path.strip()

        if "exit" in path:
            sys.exit(0)  # 正常終了時は0
            
        # 存在確認するべき
        domain = pathlib.Path(path)
        domain = domain.suffix.lower()
        if_suffix = ['.jpg', '.png', '.bmp', '.tif', '.jpeg']
        if domain in if_suffix:
            fileformat = image_checker(path,open_flag=True)
            if not isinstance(fileformat,type(None)):
                pass
            else:
                print("画像が壊れている、または画像ではないファイルです")
                print("違うファイルまたはexitを入力してください")
                continue
        elif "QR" in path:
            pass
        else:
            print("これ画像じゃないですよね...")
            print("再実行しますか？[Y/N]")
            try:
                retry = input().strip().lower()
            except UnicodeDecodeError:
                print("ファジングしようとするなあ！！！！！！！！！！！！！！！！")
                sys.exit(1)  # 異常終了時は1
            except EOFError:
                print("不正な文字列を入れてませんか？？？")
                sys.exit(1)  # 異常終了時は1
            if retry == 'y':
                continue
            elif retry == 'n':
                break
            else:
                print("リトライしてください")
                continue
        return path


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
        path = get_path()

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
                        sys.exit(0)  # 正常終了時は0
                    break
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        cv2.destroyAllWindows()

        if "http://aikatsu.com/qr/id=" in path or "AK" in path:
            print(
                """旧カツのカードは対応していません。別のカードを読み込んでください。
該当の画像を入れてください
終了する場合はexitまたはCtrl+Dでお願いします"""
            )
            del path
            continue

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
                    sys.exit(1)  # 異常終了時は1
                except UnicodeDecodeError:
                    print("ファジングしようとするなあ！！！！！！！！！！！！！！！！")
                    sys.exit(1)  # 異常終了時は1
                if retry.lower() == "y":
                    continue
                elif retry.lower() == "n":
                    break
                else:
                    print("リトライしてください")
                    continue
            except OSError:
                print("画像ファイルに見せかけた不正なファイルを読み込ませないでください")
                print("強制終了します")
                sys.exit(1)  # 異常終了時は1

            path = read[0][0].decode('utf-8', 'ignore')

        path = get_shortenURL(path)

        print(path)

        try:
            card = path['data']['url']
        except TypeError:
            print("旧カツカードまたは読み込めない形式のカードです、別のカードを読み込んでください。")
            print("該当の画像を入れてください")
            print("終了する場合はexitまたはCtrl+Dでお願いします")
            del path
            continue

        post(card)

        card = image = path = None  # 変数imageが無いのだけど...


        print("該当の画像を入れてください")
        print("終了する場合はexitまたはCtrl+Dでお願いします")


def image_first_checker(file_path):
    """
    pathを入れると画像かどうか見てくれる関数。
    最初の数バイトしか見てない為、中身が壊れていたとしても識別できない。
    
    Args:
        file_path (str or pathlib.Path): 画像ファイルのpath
    Returns:
        imgtype (str): Noneだったら画像じゃなさそう
    """
    size = os.path.getsize(file_path)
    with open(file_path) as input:
        
        data = input.read(26)
    
        if (size >= 10) and data[:6] in (b'GIF87a', b'GIF89a'):
            # GIFs
            imgtype = "GIF"
    
        elif ((size >= 24) and data.startswith(b'\211PNG\r\n\032\n')
              and (data[12:16] == b'IHDR')):
            # PNGs
            imgtype = "PNG"
    
        elif (size >= 16) and data.startswith(b'\211PNG\r\n\032\n'):
            # older PNGs
            imgtype = "PNG"
    
        elif (size >= 2) and data.startswith(b'\377\330'):
            # JPEG
            imgtype = "JPEG"
    
        elif (size >= 26) and data.startswith(b'BM'):
            # BMP
            imgtype = 'BMP'
    
        elif (size >= 8) and data[:4] in (b"II\052\000", b"MM\000\052"):
            # Standard TIFF
            imgtype = "TIFF"
    
        elif size >= 2:
            # see http://en.wikipedia.org/wiki/ICO_(file_format)
            imgtype = 'ICO'
    
        else:
            imgtype = None

    return imgtype


def image_checker(file_path,open_flag=False):
    """
    pathを入れると画像かどうか見てくれる関数。
    open_flagがfalseだと最初の数バイトしか見てない為、中身が壊れていたとしても識別できない。
    open_flagがtrueだと中身もチェックするが、遅い。
    
    image_first_checkerじゃなくてこっち使って。

    Args:
        file_path (str or pathlib.Path): 画像ファイルのpath
        open_flag (bool): falseだとimage_first_checkerのみ、trueだと実際に読み込んでみる
    Returns:
        imgtype (str): Noneだったら画像じゃなさそう
    """
    assert file_path is not None
    
    imgtype = image_first_checker(file_path)
    if open_flag and not isinstance(imgtype,type(None)):
        try:
            hoge = Image.open(file_path)
            
        except:  # 可能な限り想定される例外型を指定したほうがいいがめんどいのですべての例外で
            imgtype = None
        
    return imgtype

if __name__ == '__main__':
    main()
