import time

import requests
from bs4 import BeautifulSoup
from concurrent import futures

heards = {
    'cookie': 'sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221807e889c7acb1-00cf5411b2e24a98-977173c-1395396-1807e889c7b10c1%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fweb.shanbay.com%2F%22%7D%2C%22%24device_id%22%3A%221807e889c7acb1-00cf5411b2e24a98-977173c-1395396-1807e889c7b10c1%22%7D; _HUPUSSOID=00025a12-6910-4794-aed2-107292884eff; ua=24647624; _CLT=00376064be821b71351c003dda774e37; Hm_lvt_4fac77ceccb0cd4ad5ef1be46d740615=1651390775; Hm_lvt_b241fb65ecc2ccf4e7e3b9601c7a50de=1651390775; u=96638066|6JmO5omRSlIwOTQ1NDQyNTky|d5fa|2d86f7cc04ab2d030a25c62226478e9e|69940fcf9926fe42|aHVwdV81NjJkMmIwNDFmYjYxMWYx; us=efb651e9e14fda191b5e55ef6848b1c18f12ad0d037029668fed5e5839ae97eb425fef7e83b7e77b2ec19b2722b9c7f6093ca6e0d1ac98edb25e4ba4f061c8cc; Hm_lpvt_b241fb65ecc2ccf4e7e3b9601c7a50de=1651390848; Hm_lpvt_4fac77ceccb0cd4ad5ef1be46d740615=1651390848; SERVERID=eb24b54412b7f5b653dbf9a06cfb032f|1651390879|1651390322',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

session = requests.Session()
# 更新 hreads
session.headers.update(heards)
# 线程池
executor = futures.ThreadPoolExecutor(max_workers = 5)
links =[]
def get_link(url):
    global links
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    tags = soup.select('div.bbs-sl-web-body div.bbs-sl-web-topic-wrap div.bbs-sl-web-post ul li.bbs-sl-web-post-body a.p-title')
    links = [i['href'] for i in tags]
    return links

def comment(link):
    for i in link:
        res2 = requests.get(f'https://bbs.hupu.com{i}')
        soup2 = BeautifulSoup(res2.text,'html.parser')
        tags = soup2.select('div.bbs-post-web-body div.bbs-post-web-main div.thread-content-detail p')
        for tag in tags:
            comment = tag.text
            return comment
count =0
star = time.time()
url = 'https://bbs.hupu.com/acg'

fs =[]
for link in links:
    fs.append(
        executor.submit(comment,links)
    )
futures.wait(fs)
relust = {}
for f in fs:

    comment = f.result()
print(comment)
le = time.time()
print(f'{le - star}  时间')