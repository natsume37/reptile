import requests

session = requests.Session()
headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
# 设置 session 的全局 headers
session.headers.update(headers)
# 默认使用全局的 headers
session.get('https://wpblog.x0y1.com')
# 自定义 headers
custom_headers = { 'referer': 'https://wpblog.x0y1.com' }
session.get('https://wpblog.x0y1.com', headers=custom_headers)
'''既有全局的 user-agent 也有自定义的 referer
我们可以通过 session.headers.update() 方法来更新全局的 headers，通过该 session 发送的请求都会使用我们设置的全局 headers。

当全局 headers 不满足我们的需求时，也可以给某个请求单独设置 headers。这时，该请求将同时拥有全局和单独设置的 headers。如果两个 headers 里的字段重复，会优先使用单独设置的 headers 字段的值。

因此，之前发爬取文章的代码可以改写成下面这样：'''

import requests
from bs4 import BeautifulSoup

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
# 登录参数
login_data = {
  'log': 'codetime',
  'pwd': 'shanbay520',
  'wp-submit': '登录',
  'redirect_to': 'https://wpblog.x0y1.com',
  'testcookie': '1'
}

session = requests.Session()
session.headers.update(headers)
# 使用 session 登录
login_req = session.post('https://wpblog.x0y1.com/wp-login.php', data=login_data)
# 使用 session 获得 Python 分类文章
comment_req = session.get('https://wpblog.x0y1.com/?cat=2')

# 解析页面
soup = BeautifulSoup(comment_req.text, 'html.parser')
# 选择所有的代表标题的 a 标签
titles = soup.select('h2.entry-title a')
# 获取四篇文章的链接
links = [i.attrs['href'] for i in titles]

for link in links:
  # 获取文章页面内容
  res_psg = session.get(link)
  # 解析文章页面
  soup_psg = BeautifulSoup(res_psg.text, 'html.parser')
  # 获取文章内容的标签
  content = soup_psg.select('div.entry-content')[0]
  # 打印文章内容
  print(content.text)