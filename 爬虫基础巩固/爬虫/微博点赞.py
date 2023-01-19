import requests

class WeiboSpider:
  def __init__(self):
    self.session = requests.Session()
    self.headers = {
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
      'mweibo-pwa': '1',
      'x-requested-with': 'XMLHttpRequest',
      'cookie': '你的cookie'
    }
    self.session.headers.update(self.headers)

  def get_st(self):
    config_headers = {
      'origin': 'https://m.weibo.cn/',
      'referer': 'https://m.weibo.cn/'
    }
    self.session.headers.update(config_headers)

    config_req = self.session.get('https://m.weibo.cn/api/config')
    config = config_req.json()
    st = config['data']['st']
    return st

  def compose(self, content, st):
    compose_headers = {
      'origin': 'https://m.weibo.cn/',
      'referer': 'https://m.weibo.cn/compose/',
      'x-xsrf-token': st
    }
    self.session.headers.update(compose_headers)

    compose_data = {
      'content': content,
      'st': st
    }
    compose_req = self.session.post('https://m.weibo.cn/api/statuses/update', data=compose_data)
    print(compose_req.json())

  def send(self, content):
    st = self.get_st()
    self.compose(content, st)

  # 获取微博列表
  def get_weibo_list(self):
    params = {
      'sudaref': 'security.weibo.com',
      'type': 'uid',
      'value': '2139359753',  # 扇贝官微 id
      'containerid': '1076032139359753'
    }
    weibo_list_req = self.session.get('https://m.weibo.cn/api/container/getIndex', params=params)
    weibo_list_data = weibo_list_req.json()
    weibo_list = weibo_list_data['data']['cards']
    return weibo_list

  # 点赞微博
  def vote_up(self, id):
    vote_up_data = {
      'id': id,  # 要点赞的微博 id
      'attitude': 'heart',
      'st': self.get_st()
    }
    vote_up_req = self.session.post('https://m.weibo.cn/api/attitudes/create', data=vote_up_data)
    json = vote_up_req.json()
    print(json['msg'])

  # 批量点赞微博
  def vote_up_all(self):
    st = self.get_st()
    vote_headers = {
      'x-xsrf-token': st
    }
    self.session.headers.update(vote_headers)
    weibo_list = self.get_weibo_list()
    for i in weibo_list:
      # card_type 为 9 是正常微博
      if i['card_type'] == 9:
        self.vote_up(i['mblog']['id'])

weibo = WeiboSpider()
weibo.vote_up_all()