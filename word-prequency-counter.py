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
			# print (eword)
			wordlist.append(eword)
	clean_up_list(wordlist)

def clean_up_list(wordlist):
	clear_word_list = []
	for word in wordlist:
		sysbols = "!?.@#@%&_+:\"“”<>?./;'[]-=',"
		for i in range(0, len(sysbols)):
			word = word.replace(sysbols[i], "")
		if(len(word) > 0):
			# print(word)
			clear_word_list.append(word)
	create_dictionary(clear_word_list)

def create_dictionary(clear_word_list):
	word_count = {}
	for word in clear_word_list:
		if (word in word_count):
			word_count[word] += 1
		else:
			word_count[word] = 1
	for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
		print(key, value)
start('https://dantri.com.vn/the-gioi.htm')
# start('http://hdsieunhanh.com/filter/trang-1.html')

def nothing():
	pass
