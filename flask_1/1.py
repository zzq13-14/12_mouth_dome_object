import requests
import random
import MyUserAgent
from lxml import etree
# import time
# from s12_project.modle import *
from music_sql import *
# from sqlalchemy.orm import sessionmaker
headers = {
    'User-Agent': random.choice(MyUserAgent.my_chorme_agent)
}
urls=[
    'http://www.hao123.com/music/wangzhi',
      # 'http://music.taihe.com/?fr=hao123',
       # 'http://www.app-echo.com/#/'
    # 'http://www.dj97.com/'
    # 'https://music.163.com/'
    'http://www.djkk.com/'
      ]


#创建类的对象,添加数据
def  connent_sql(tt,abc):

    info=Music(music_title=tt,music_url=abc)
    db.session.add(info)
    db.session.commit()
    print('数据添加完成')

for url in urls:
    res=requests.get(url,headers=headers)
    soup = etree.HTML(res.text, etree.HTMLParser())
    herolist = soup.xpath('//a[@onclick="return Listen(this.href);"]')#歌曲链接
    herolist_title2 = soup.xpath('//dd[@class="layui-col-xs11 layui-col-sm11 layui-elip"]/a')#歌曲名字
# print(len(herolist_title2))
# print(herolist_title2)

    with open('dj.html', 'w+', encoding='utf-8')as f:
        f.write('<html lang="en">' + '\n')
        f.write('<head>' + '\n')
        f.write('<meta charset = "UTF-8" >' + '\n')
        f.write('<title> DJ音乐网 </title>'+'\n')
        f.write('</head>' + '\n')
        f.write('<body>' + '\n')
        # print(len(tt))
        # nn=1
        for index,i in enumerate(herolist):
            res = i.get('href')#歌曲url
            tt = herolist_title2[index].get('title')  # 歌曲名
            ress = res.replace('..', '')
            abc = 'http://www.djkk.com' + ress
            # print(abc)
            connent_sql(tt,abc)
            f.write(
                '<a style="font-size:18px;color:blue;font-weight:bold;  display: block;" href=' + abc + '>' + tt + '</a>')
            f.write('\n')
        f.write('</body>' + '\n')
        f.write('</html>')
# connent_sql()
