import requests

list = 20


def pa(list, n):
    url = f'https://spa1.scrape.center/api/'

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    params = {
        'limit': list,
        'offset': n * 10
    }
    re = requests.get(url, headers=header, params=params)
    print(re.json())


pa(20, 10)
