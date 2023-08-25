import json
from module import sc_ctrl as main

with open('urls.json') as f:
    urls = json.load(f)

url_main = urls['url_main']#ホームページ
url_songs = url_main + urls['url_songs']#'#収録楽曲一覧のページ

main.run(url_main, url_songs)
