import requests
import random
import MyUserAgent
from lxml import etree
from music_sql import *

headers={
    'User-Agent':random.choice(MyUserAgent.my_chorme_agent)
}
urls=[
    # 'http://www.hao123.com/music/wangzhi',
    'http://www.djkk.com/'
      ]
def  connent_sql(tt,abc,real_audio_url):

    info=Music(music_title=tt,music_url=abc,music_url_audio=real_audio_url)
    db.session.add(info)
    db.session.commit()
    print('数据添加完成')

for url in urls:
    res=requests.get(url,headers=headers)
    html=etree.HTML(res.text,etree.HTMLParser())
    music_url=html.xpath('//a[@onclick="return Listen(this.href);"]')
    music_title=html.xpath('//dd[@class="layui-col-xs11 layui-col-sm11 layui-elip"]/a')
    # print(music_url)
    # print(music_title)
    # for i in music_title:
    #     t=i.text
    # for u in music_url:
    #     ur=u.get('href')


    with open('dj.html', 'w+', encoding='utf-8')as f:
        f.write('<html lang="en">' + '\n')
        f.write('<head>' + '\n')
        f.write('<meta charset = "UTF-8" >' + '\n')
        f.write('<title> DJ音乐网 </title>'+'\n')
        f.write('</head>' + '\n')
        f.write('<body>' + '\n')
        # print(len(tt))
        # nn=1
        for index,i, in enumerate(music_url):
            res = i.get('href')#歌曲url
            tt = music_title[index].get('title')  # 歌曲名
            ress = res.replace('..', '')
            abc = 'http://www.djkk.com' + ress
            url = abc
            res = requests.get(url)
            # print(res.status_code)
            # print(res.text)

            # print(re.findall(r'', res.text))
            res_text = res.text
            start_index = res_text.find('list=[{title:')
            str_1 = res_text[res_text.find('list=[{title:'):]
            str_2 = str_1[str_1.find('m4a') + 4:]
            real_audio_url = str_2[str_2.find('"') + 1:str_2.find('}') - 1]
            print(real_audio_url)
            connent_sql(tt, abc, real_audio_url)
            # print(abc)



            # for i in abc:
                # print(i.music_url)

                # url = 'http://www.djkk.com/dance/play/395260.html'
                # url = i.music_url

            f.write(
                '<a style="font-size:18px;color:blue;font-weight:bold;  display: block;" href=' + abc + '>' + tt + '</a>')
            f.write('\n')
        f.write('</body>' + '\n')
        f.write('</html>')