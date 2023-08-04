import os
import traceback
import shutil
from module import songs_class as sc
from module import get_soup as gs

def run(url_main, url_songs):
    try:
        main_soup = gs.get_soup(url_songs)
        Songs = sc.songs(main_soup, url_main, url_songs)
    except Exception as e:
        print(traceback.format_exception_only(type(e), e)[0])
        return
    
    print('プロジェクトセカイ攻略Wiki(https://pjsekai.com/)からスクレイピングしています。\n')
    song_width = int(shutil.get_terminal_size().columns) // 3 - 6
    if song_width < 39:
        print('ターミナルの横幅を広くしておいたほうが表示がいい感じになります。\n')

    orders = [1, 2, 3, 9]
    while(True):
        print('数字を入力してください')
        print('1:曲一覧の表示')
        print('2:masterの難易度指定で表示')
        print('3:ジャケットのダウンロード')
        print('9:終了')
        
        num = int_validate(input())
        if num == False:
            input('press enter')
            clear()
            continue
        elif num not in orders:
            print('適切な数字を入力してください')
            input('press enter')
            clear()
            continue
        
        if num == 1:
            Songs.display_songs()
        elif num == 2:
            Songs.display_ms_specify()
        elif num == 3:
            Songs.get_image()
        elif num == 9:
            print('終了します。')
            input('press enter')
            clear()
            break

        input('press enter')
        clear()

def clear():
    os.system('cls')

def int_validate(n):
    try:
        n = float(n)
        if n % 1 != 0:
            print('適切な数字をを入力してください')
            return False
        return int(n)
    except Exception as e:
        print('適切な数字を入力してください')
        return False
