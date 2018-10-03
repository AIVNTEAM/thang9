# requests for fetching html of website
import requests
# regex lib
import re
import xlsxwriter

# Make the GET request to a url
r = requests.get('http://pdu.edu.vn/nss.php?name=DanhBa&search=true&hoten=&phongban=28')
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
main_content = soup.find('table', attrs = {'style': 'font-size:12px;'})

# print main_content
content = main_content.find_all('td')#.get_text().encode('utf-8')
print content

#tao workbook va add worksheet
workbook = xlsxwriter.Workbook('data2.xlsx')
worksheet = workbook.add_worksheet('Sheet 1')
for i in range(1, len(content)):
	if (i % 3 == 0):
		worksheet.write(i, 0, content[i].text)
	elif (i % 3 == 1):
		worksheet.write(i, 1, content[i].text)   		
	else:
		worksheet.write(i, 2, content[i].text)
    	
workbook.close()
