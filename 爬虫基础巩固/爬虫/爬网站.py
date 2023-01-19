import requests
import time
from bs4 import BeautifulSoup
from openpyxl import Workbook

#创建一个 书名表
wb = Workbook()
sheet = wb.active
sheet.title = '豆瓣图书统计表'
# 写入表头
header = ['书名',  '链接']
sheet.append(header)

# 爬取信息
def get_douban_movies(url):
  headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
  }
  res = requests.get(url, headers=headers)
  soup = BeautifulSoup(res.text, 'html.parser')
  # 电影信息在 class='hd' 的 div 标签里
  items = soup.find_all('div', class_='hd')
  for i in items:
    tag = i.find('a')
    # 取 a 标签里的第一个 class='title' 的内容为电影名
    name = tag.find(class_='title').text
    # a 标签上有链接
    link = tag['href']
    row = [name, link]
    sheet.append(row)

    print(row)

url = 'https://movie.douban.com/top250?start={}'
urls = [url.format(num * 25) for num in range(10)]
for i in urls:
  get_douban_movies(i)
  time.sleep(1)


# 关闭保持表
wb.save('豆瓣图书统计.xlsx')