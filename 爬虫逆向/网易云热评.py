"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : 网易云热评.py
@Author : 夏目&青一
@Time : 2022/11/4 21:20

"""
import requests

url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

header = {
    'origin': 'https://music.163.com',
    'cookie': '_iuqxldmzr_=32; _ntes_nnid=c531227e9444f2bfc5b84be6e4c31522,1667567849317; _ntes_nuid=c531227e9444f2bfc5b84be6e4c31522; NMTID=00OfB5j4dWo_MKcfkX8pS9TkWVrKAMAAAGEQsoPUw; WEVNSM=1.0.0; WNMCID=tbbxki.1667567849630.01.0; WM_TID=IAaWWOx3V6NEVBBEQFKQNSAJsd0CHb2j; JSESSIONID-WYYY=yYVvIP%2BYng8qTOCZhy1PccsFj%2BKerkgeGJkSRhtst%2Bxxk1HEp22imak5VDsKDgkU6il5y1HYn2zc7ytulxZWmbjemS8YMVmdPglQPdC%5CKNYQU%2BbbQJs7OT4S6lAR6xSfnX9TPjPioYy1E8eK3E4dt%5Cp69zgxIBdJ%2BlRiwtXMK%2BAkB5ca%3A1667734443690; WM_NI=ZZD3y9oJWQFZeLtgiJ8RNYXSz%2BCnWngbWXYyAPItnDFX4VttwPlTAGFh9RcNOwBRapU9NOcO8jYnNTuiwLZ9K%2F7sjoBSUsx04iVv8wkrzaeUtyJHFU86XppHfkB24hRucW4%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee83d37ba8a88382b845acef8fb6d14a979e8eacd546819cff8caa448b939cd1f12af0fea7c3b92a9a868cd4fc33ad9699b2c552a794bc88ec42fc8e82badb59baf58d8fd666a5be99b9dc7383908795ed508688fcb7f780b590a4b5c44d86b8f7b3e2468da98eb3e47c97e782b0e245fcb6978fcd60b7b7b9add93389f1f994e965828d9b94fb3cf8b79a97bb7da9aeb682e85fb8a786a9c55ffcea9891f344a6b58ed3b76492abadb8b737e2a3',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
    'referer': 'https://music.163.com/song?id=865632948&market=baiduqk'

}
data = 'params=8MK1tpxXuhde0cjZ%2F1MfqWdSJn%2BjLkQWL3yt2tlKZrpjgd4YnKxnaX%2BE%2BQ%2B7hGFYrxAJgM5NI50bOJvOLtDwGnVclFfUW43WmO1XKims%2FLmwcI%2FH4OnojxcbNUvHGdlbobDo2z%2F2uFPdEyGs3%2Bakg%2BW3yX%2Fd6jndn8geKn%2BRAaA3P7ApSgLlmrM%2FozP3IbCI0nrKXsbout3qxKeX3nhS5H%2B9Z8%2BBJrV05l4XlwlYk1moX4JJUHvy6wQI4dBXrBpW42U71M5if4V4q1NEAkTFPpn%2FwmX8zfg%2F6o9Gz%2BjUGfM%3D&encSecKey=3167d58d407b09296d142b066a9e929c11e76af1423cb43a6f4e971ec005eda624fa75241d65c221bc1421dd57a00e007f90c0920c63ee8c55646d63b849e2157d93fc4c1e68db1049897e0738c17ae1a89da5a8a4a0458caaa9ce3eee4535b8036e066ee0c067acab0727477afbb7148d4337ac7274e80b9a564d6e69aca21c'
re = requests.post(url,headers=header,params=data)
print(re.status_code)
print(re.history)
# res = re.json()['data']['hotComments']
# for i in res:
#     coment = i['content']
#     dianzhan = i['likedCount']
#     print(f'content,{coment}',end='\t')
#     print(dianzhan)