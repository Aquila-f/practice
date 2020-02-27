import requests
import re
from bs4 import BeautifulSoup

res = requests.get('https://www.coolpc.com.tw/evaluate.php')
# res.encoding = 'utf8'
page = res.text
soups = BeautifulSoup(page,'html.parser')


print('輸入查找項目列表')
targetnum = int(input())-1
targetsel = soups.find_all("tr",{'bgcolor':['efefe0']})[targetnum]


print(targetsel)
# cpu = soups.find_all('optgroup',{'label'}



