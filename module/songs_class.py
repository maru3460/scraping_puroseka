import os
import requests
from bs4 import BeautifulSoup
import unicodedata as uni
import traceback
import shutil
from module import get_soup as gs

class songs():
    def __init__(self, soup, url_main, url_songs):
        self.url_main = url_main
        self.url_songs = url_songs

        table = soup.find(id = 'sortable_table1')
        tmp = table.find('tbody')

        self.songs_orig = tmp.find_all('td')
        self.inf_sum = 17
        self.song_name = 3
        self.song_expert = 8
        self.song_master = 9
        self.songs_sum = len(self.songs_orig) // self.inf_sum

        self.songs_arr = []
        for i in range(self.songs_sum):
            tmp = []
            for j in range(self.inf_sum):
                tmp.append(str(self.songs_orig[i * self.inf_sum + j].string))
            self.songs_arr.append(tmp)
        
        '''
        データ指定
        table id : sortable_table1 > tbody > td class : style_td 一行17個
        '''
    
    def cul_HalfCharNum(self, s):
        return sum([(1, 2)[uni.east_asian_width(t) in 'FWA'] for t in s])
    
    def display_songs(self):
        song_width = int(shutil.get_terminal_size().columns) // 3 - 6

        for i in range(self.songs_sum):
            name = self.songs_arr[i][self.song_name]
            lengh = len(name) + (song_width - self.cul_HalfCharNum(name))
            print('{index:^3}:{tmp_name:<{tmp_lengh}}'.format(index = i + 1, tmp_name = name, tmp_lengh = lengh), end='')
            if i > 0 and i % 3 == 2:
                print()
        print()
    
    def get_image(self):
        img_file_path = 'saved_images'

        self.display_songs()
        print('曲の数字を入力してください')
        song_index = int_validate(input())
        if song_index == False:
            return
        elif song_index < 1 or self.songs_sum < song_index:
            print('適切な数字を入力してください')
            return

        if not os.path.isdir(img_file_path):
            os.mkdir(img_file_path)

        img_url = gs.search_img_url(self.songs_orig, self.url_main, self.inf_sum, self.song_name, song_index)
        if img_url:
            try:
                file_path = 'saved_images/image' + str(song_index) + '.jpg'
                res_img = requests.get(img_url)
                img = res_img.content
                with open(file_path, "wb") as f:
                    f.write(img)
            except Exception as e:
                print(traceback.format_exception_only(type(e), e)[0])
                print('画像の保存に失敗しました。')
                return
        else:
            return
        print(f'{self.songs_arr[song_index - 1][self.song_name]}の画像をダウンロードできました。')
    
    def display_ms_specify(self):
        song_width = int(shutil.get_terminal_size().columns) // 3 - 6

        print('難易度を入力してください')
        song_dif = int_validate(input())
        if song_dif == False:
            return
        
        tmp = []
        for i in range(self.songs_sum):
            if int(self.songs_arr[i][self.song_master]) == song_dif:
                tmp.append(self.songs_arr[i][self.song_name])
        if len(tmp) == 0:
            print('この難易度の曲は存在しません。')
            return
        tmp.sort()

        print(f'Master難易度{song_dif}の曲一覧')
        for i in range(len(tmp)):
            lengh = len(tmp[i]) + (song_width - self.cul_HalfCharNum(tmp[i]))
            print('{tmp_name:<{tmp_lengh}}'.format(tmp_name = tmp[i], tmp_lengh = lengh), end='')
            if i > 0 and i % 3 == 2:
                print()
        print()
        return



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