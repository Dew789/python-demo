from urllib import request
from bs4 import BeautifulSoup

url = input('Enter _ ')
html = request.urlopen(url).read()
html = html.decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
total = 0
for tag in tags:
    num = int(tag.contents[0])
    total += num
print(total)
