import random
import urllib.request

def download_web_img(url):
	name = random.randrange(1,2000)
	fullname = str(name) + ".jpg"
	urllib.request.urlretrieve(url, fullname)

download_web_img('https://vnn-imgs-f.vgcloud.vn/2018/09/18/13/an-tuong-hinh-anh-ngoai-giao-xe-hoi-moon-kim-tren-duong-pho-binh-nhuong.jpg')