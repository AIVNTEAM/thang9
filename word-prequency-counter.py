import requests
from bs4 import BeautifulSoup
import operator

def start(url):
	wordlist = []
	souce_code = requests.get(url)
	plan_text = souce_code.text
	# print(plan_text)
	soup = BeautifulSoup(plan_text, 'html.parser')
	for post_text in soup.findAll('a', {'class': 'fon6'}):
		content = post_text.string
		# print(content)
		words = content.lower().split()
		for eword in words:
			print (eword)
			wordlist.append(eword)
start('https://dantri.com.vn/the-gioi.htm')
# start('http://hdsieunhanh.com/filter/trang-1.html')
