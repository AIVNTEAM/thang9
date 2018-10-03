# requests for fetching html of website
import requests
# regex lib
import re

# Make the GET request to a url
r = requests.get('http://trongtanviet.com/bao-gia-trong-truong-hoc-20172018_i1930_c434.aspx')
# r.encoding = "utf-8"
r.encoding = 'utf-8'

# Extract the content
c = r.content

from bs4 import BeautifulSoup

# Create a soup object
soup = BeautifulSoup(c, "html.parser")
soup.encode('utf-8')

# print soup
# Find the element on the webpage
main_content = soup.find('div', attrs = {'class': 'proname'})
abc = main_content.find('h1').text
print abc.encode('utf-8')
