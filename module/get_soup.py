import requests
from bs4 import BeautifulSoup
import traceback

def get_soup(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    return BeautifulSoup(res.text, 'html.parser')

def search_img_url(songs_orig, url_main, inf_sum, song_name, song_index):
    try:
        #付加するurl(指定曲のページ)を取得
        tmp = songs_orig[inf_sum * (song_index - 1) + song_name].find('a')
        tmp = tmp.get('href')
        page_add_url = tmp.lstrip()

        #リンク先のページを取得
        res_img_page = requests.get(url_main + page_add_url)
        res_img_page.encoding = 'utf-8'
        soup_img_page = BeautifulSoup(res_img_page.text, 'html.parser')

        #付加するurl(画像)を取得
        tmp = soup_img_page.find('p')
        tmp = tmp.find('img')
        tmp = str(tmp.get('data-src'))
        tmp = tmp.lstrip()
        img_add_url = tmp.replace('amp;', '')
        img_url = url_main + img_add_url

        return img_url
    except Exception as e:
        print(traceback.format_exception_only(type(e), e)[0])
        print('画像のURLの取得に失敗しました。')
        return False
    

    
    '''htmlの変更によって動かなくなる恐れ大
    <h2 id="content_1_0">
        Tell Your World  
        <a class="anchor_super" id="fcbcfcd0" href="./?708ecb0c47#fcbcfcd0" title="fcbcfcd0" style="user-select:none;">
            &#8204;
        </a>
        <a class="anchor_super" href="https://pjsekai.com/?cmd=secedit&amp;page=Tell%20Your%20World&amp;id=1&amp;level=true" title="Edit"> 
            <img src="image/paraedit.png" width="9" height="9" alt="Edit" title="Edit" />
        </a>
    </h2>

    <p>
        <div class="tag">
            Tag: 
                <a href="https://pjsekai.com/?cmd=taglist&amp;tag=VirtualSinger">
                    VirtualSinger
                </a> , 
                <a href="https://pjsekai.com/?cmd=taglist&amp;tag=kz%28livetune%29">
                    kz(livetune)
                </a> , 
                <a href="https://pjsekai.com/?cmd=taglist&amp;tag=CM%E3%82%BD%E3%83%B3%E3%82%B0">
                    CMソング
                </a> , 
                <a href="https://pjsekai.com/?cmd=taglist&amp;tag=%E3%82%BD%E3%83%AD3DMV">
                    ソロ3DMV
                </a> , 
        </div>
        <br />
        <img class="lazyload" src="image/spacer.png" data-src="./?plugin=ref&amp;page=Tell%20Your%20World&amp;src=Tell%20Your%20World.jpg" alt="Tell Your World.jpg" title="Tell Your World.jpg" width="350" height="350" />
    </p>

    https://pjsekai.com/?plugin=ref&page=Tell%20Your%20World&src=Tell%20Your%20World.jpg
    '''