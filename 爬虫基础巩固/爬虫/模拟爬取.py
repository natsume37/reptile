import requests
img = f"//img2.huashi6.com/images/resource/thumbnail/2021/11/13/14208_40890869520.jpg?imageMogr2/quality/75/interlace/1/thumbnail/700x/gravity/North/crop/700x1070/format/jpeg%7Cwatermark/2/text/6Kem56uZQEFz6ZqQ5aOr54yr/gravity/South/fill/I2ZmZmZmZg/fontsize/400/font/5b6u6L2v6ZuF6buR/dy/20"

url = f"https:{img}"

print(url.split('/')[-1])
r = requests.get(url)
image = r.content
with open('name.png', 'wb') as f:
    f.write(image)