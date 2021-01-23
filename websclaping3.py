import requests
from bs4 import BeautifulSoup

url='https://www.nikkei.com/markets/worldidx/'

res=requests.get(url)
soup=BeautifulSoup(res.content)

table=soup.find('table','cmn-table_style1')
trs=table.findAll('tr')

result={}
for tr in trs:
    th=tr.find('th')
    tds=tr.findAll('td')
    # print(th.text)
    # print(tds[1].text)
    cleaned_th=th.text.replace('\xa0','').replace('※','')
    result[cleaned_th]=tds[0].text
print(result)
