import requests
from lxml import etree
from s11月机试考试.User_agent_name import my_chrome_agent
import random
from s12_project.modle import *
import re
headers={
    'User-Agent':random.choice(my_chrome_agent)
}
# proxies={

# }


#连接数据库
def connent_sql(player_title,player_url):
    player_music=Music_Player(player_title=player_title,player_url=player_url)
    db.session.add(player_music)
    db.session.commit()

#获取网址URL
def get_url():
    urls=[
        'http://www.hao123.com/music/wangzhi',
          # 'http://music.taihe.com/?fr=hao123',
           # 'http://www.app-echo.com/#/'
        # 'http://www.dj97.com/'
        # 'https://music.163.com/'
          ]
    for url in urls:
        res=requests.get(url,headers=headers)
        res.encoding=res.apparent_encoding
    # print(res.text)
	
	#解析网页
        soup=etree.HTML(res.text,etree.HTMLParser())
        list_info=soup.xpath('//a[@class="text-con"]')#主网页url
        list_info1=soup.xpath('//a[@class="text-con"]')#主网页title
        # list_info1=soup.xpath('//a[@class="img-wrapper pr"]')#千千音乐界面
        list_info2=soup.xpath('//div[@id="top-flag"]')#千千音乐界面
        # list_info2=soup.xpath('//img[@class="pic"]/@src')#echo界面
        list_info3=soup.xpath('//a[@target="play"]')#dj界面
        list_info4=soup.xpath('*//ol')#网易云
        # print(len(list_info))
        # print(list_info)

		
	#保存文件
        with open('hao_123_music.html','w',encoding='utf8')as f:
            f.write('<html lang="en">'+'\n')
            f.write('<head>'+'\n')
            f.write('<meta charset = "UTF-8">'+'\n')
            f.write('<title>hao_123</title>'+'\n')
            f.write('</head>'+'\n')
            f.write('<body>'+'\n')
            n=1
            for index,i in enumerate(list_info):
                player_url=i.get('href')
                player_title=list_info[index].text
                # print(player_title,player_url)
                f.write('<a style="font-size:25px;color:pink;font-weight:bold;display:block;" href='+player_url+'>'+str(n)+player_title+'</a>')
                f.write('\n')
                n+=1
                connent_sql(player_title,player_url)
            f.write('</body>'+'\n')
            f.write('</html>')
            print('下载ok')

get_url()






