"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : 并发结业项目.py
@Author : 夏目&青一
@Time : 2022/11/16 20:04

"""
"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : 爬虫结业项目.py
@Author : 夏目&青一
@Time : 2022/11/16 18:52

"""

import requests

url = 'https://apic.liepin.com/api/com.liepin.searchfront4c.pc-search-job'

# 简化后的消息头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
    'Cookie': 'inited_user=283b142cf463effbb16544a569780fe4; __gc_id=f76aa46e3c6c4877ac956dcf4bdbf90f; __s_bid=2f367c6a8f7c3e56bc32043e736c2c1b05e2; __uuid=1651718614300.57; need_bind_tel=false; c_flag=b54508d4d70eee8e6e5d6a91e9c3a2ac; XSRF-TOKEN=mT8-CPYPSdyIBSedI7mCiA; __tlog=1668595735240.11%7C00000000%7C00000000%7C00000000%7C00000000; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1668595735; acw_tc=276077cf16685957395552767ec4d7ccf2fa8915ca89b0070ccdc47b12ab95; UniqueKey=ef245d2ddfa80c86a9dba665e9526a14; lt_auth=s%2BcKaCYMml%2F%2F4nnaiWRb4P1Nht38UT6apXUM0xgFgtftX%2FGz4P%2FgQgyHr7EB%2FioIq0x3Jv0zMLb4Pe33zHtN7kcR8VGnlZ6uvPK%2Bz3YHUeZjHuyflMXuqsjQQ5wtrXg6ykpgn2si; access_system=C; user_roles=0; user_photo=5f8fa3a679c7cc70efbf444e08u.png; user_name=%E4%B8%81%E6%A0%91%E9%9D%92; new_user=false; inited_user=283b142cf463effbb16544a569780fe4; __session_seq=4; __uv_seq=4; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1668595871; imClientId=a8f0406d267ffd18da81bbaa5ce04b53; imId=a8f0406d267ffd18a2a0dbc25353d58f; imClientId_0=a8f0406d267ffd18da81bbaa5ce04b53; imId_0=a8f0406d267ffd18a2a0dbc25353d58f; imApp_0=1; fe_im_socketSequence_new_0=1_0_1; fe_im_opened_pages=; fe_im_connectJson_0=%7B%220_ef245d2ddfa80c86a9dba665e9526a14%22%3A%7B%22socketConnect%22%3A%222%22%2C%22connectDomain%22%3A%22liepin.com%22%7D%7D',
    # 约定请求体为 JSON 格式数据
    'Content-Type': 'application/json;charset=UTF-8',
    # 应对猎聘网反爬机制
    'X-Client-Type': 'web',
    'X-Fscp-Bi-Stat': '{"location": "https://www.liepin.com/zhaopin/?city=410&dq=410&pubTime=&currentPage=0&pageSize=40&key=python&suggestTag=&workYearCode=&compId=&compName=&compTag=&industry=&salary=&jobKind=&compScale=&compKind=&compStage=&eduLevel=&otherCity=&scene=input&suggestId="}',
    'X-Fscp-Fe-Version': '6482016',
    'X-Fscp-Std-Info': '{"client_id": "40108"}',
    'X-Fscp-Trace-Id': 'fa62ab24-6bd6-46f9-a749-5749913bd603',
    'X-Fscp-Version': '1.1',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'mT8-CPYPSdyIBSedI7mCiA'
}

nub = 1
# 程序开始


for i in range(15):
    json = {"data": {
        "mainSearchPcConditionForm": {"city": "410", "dq": "410", "pubTime": "", "currentPage": i, "pageSize": 40,
                                      "key": "python", "suggestTag": "", "workYearCode": "", "compId": "",
                                      "compName": "",
                                      "compTag": "", "industry": "", "salary": "", "jobKind": "", "compScale": "",
                                      "compKind": "", "compStage": "", "eduLevel": ""}}}

    res = requests.post(url, headers=headers, json=json)

    tag = res.json()['data']['data']['jobCardList']

    for i in tag:
        title = i['job']['title']
        salary = i['job']['salary']
        comp_name = i['comp']['compName']
        print(f'{nub}\t岗位名 {title}\t工资  {salary}\t公司名   {comp_name}')
        nub += 1
