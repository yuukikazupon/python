# import requests
# from bs4 import BeautifulSoup
#
# url='https://news.yahoo.co.jp/flash?p=1'
# res=requests.get(url)
# soup=BeautifulSoup(res.content)
# parent=soup.find('div','newsFeed')
# targets=parent.findAll('div','newsFeed_item_title')
#
# for target in targets:
#     print(target.text)
import requests
from bs4 import BeautifulSoup

url='https://news.yahoo.co.jp/flash?p=1'
res=requests.get(url)
soup=BeautifulSoup(res.content)
parents=soup.findAll('div','flashSummary')
# print(parents)
for parent in parents:
    targets=parent.findAll('p','flashSummary_title')
    for target in targets:
        print(target.text)
# targets=parent.findAll('p','flashSummary_title')
