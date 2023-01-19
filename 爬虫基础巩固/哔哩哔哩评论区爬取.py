"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : 哔哩哔哩评论区爬取.py
@Author : 夏目&青一
@Time : 2022/10/27 14:37

"""

import requests

count = 0
# url = 'https://api.bilibili.com/x/v2/reply/main?csrf=09379e8bb44fbb17c4f28371bd64d499&mode=3&next=0&oid=302231426&plat=1&seek_rpid=&type=1'
url = 'https://api.bilibili.com/x/v2/reply/main?callback=jQuery17209381224907341732_1666856276249&jsonp=jsonp&next=0&type=1&oid=71422691&mode=3&plat=1&_=1666856278214'

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'origin': 'https://www.bilibili.com',
    'cookie': r"buvid3=02DEC325-F47A-CD07-5CB2-D6B58A8A195660049infoc; b_nut=1665751460; i-wanna-go-back=-1; _uuid=582B1051D-F3EE-1134-4B89-1082A9CCA10B4658520infoc; buvid4=D02E3E0A-C064-DAAA-F07E-E1EA31D9F7BD61940-022101420-8PVRJZxYu3Xb/cLwXOaOUg%3D%3D; fingerprint=b70a63179a94bd888994f6d20c854da7; buvid_fp_plain=undefined; DedeUserID=646388511; DedeUserID__ckMd5=aa2695afa6fbadc4; buvid_fp=abfecfa8ba50e80c8b8350543c5219b5; b_ut=5; rpdid=|(k|kY||R~Yk0J'uYYl~lk|Rm; bp_video_offset_646388511=717594958374109200; nostalgia_conf=-1; CURRENT_QUALITY=80; bsource=search_google; b_lsid=14444C2F_184181F7CB0; SESSDATA=1bfc22a7%2C1682404028%2C9b6be%2Aa1; bili_jct=09379e8bb44fbb17c4f28371bd64d499; sid=6m76ovjl; innersign=1; PVID=2; CURRENT_FNVAL=4048",
    'referer': 'https://www.bilibili.com/video/BV1UP411j71N/?spm_id_from=333.337.search-card.all.click&vd_source=1a5796df38d45b002f615567954d7129'
}
re = requests.get(url, headers=header)
try:
    file = open(r"C:\Users\19570\Desktop\哔哩哔哩.txt",'a+')
    if re.status_code == 200:
        print(type(re.json()))
        xhl = re.json()['data']['replies']
        for i in xhl:
            content = i['content']['message']
            mid = i['member']['mid']
            use_name = i['member']['uname']
            sex = i['member']['sex']
            signature = i['member']['sign']
            tity = i['reply_control']['location']
            count += 1
            print(f' {count}\nuname: {use_name}\nmid: {mid}\nsex: {sex}\ntity: {tity}')
            print(f'sign: {signature}')
            print(f'message: {content}')
            print()
            file.write(f'  {count}  uname: {use_name}\nmid: {mid}\nsex: {sex}\ntity: {tity}\nsign: {signature}\nmessage: {content}\n')

    file.close()
except :
    file.close()