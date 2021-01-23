import requests
from bs4 import BeautifulSoup

for i in range(1,41):
    url='https://news.yahoo.co.jp/flash?p={}'.format(str(i))
    res=requests.get(url)
    soup=BeautifulSoup(res.content)
    parents=soup.findAll('div','flashSummary')
    # print(parents)
    for parent in parents:
        targets=parent.findAll('p','flashSummary_title')
        for target in targets:
            print(target.text)
