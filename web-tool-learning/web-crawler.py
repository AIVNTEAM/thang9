import requests
from bs4 import BeautifulSoup

def film_trader(max_pages):
	page = 1
	while page <= max_pages:
		url = 'http://hdsieunhanh.com/filter/trang-' + str(page) + '.html'
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text)
		for link in soup.findAll('a', {'class': 'film-small'}):
			href = link.get('href')
			print (href)
			title = link.get('title')
			print (title)
		page += 1
film_trader(2)