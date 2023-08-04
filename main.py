from module import sc_ctrl as main

url_main = 'https://pjsekai.com'
url_songs = url_main + '/?aad6ee23b0'#収録楽曲一覧のページ

main.run(url_main, url_songs)
