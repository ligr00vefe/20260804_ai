import bs4
import urllib.request

# url = "https://www.nate.com"
# htmlObj = urllib.request.urlopen(url)
# webPage = htmlObj.read()
# bsObj = bs4.BeautifulSoup(webPage, 'html.parser')
#
# tag = bsObj.find('div', {'id': 'divGnb'})
#
# tag.find_all('li')
# for item in tag:
#   print(item.text, end=' ')
# print()

url = "http://go.busanitacademy.com/shop/list.php?ca_id=10&gclid=EAIaIQobChMIuKDt0_y5iAMV92oPAh1J6g2xEAAYAyAAEgK4d_D_BwE"
htmlObj = urllib.request.urlopen(url)
webPage = htmlObj.read()
bsObj = bs4.BeautifulSoup(webPage, 'html.parser')
# print(bsObj)
tag = bsObj.find('ul', {'class': 'maingnb'})
# print(tag)
tags = tag.find_all('span')
# print(tags)
for item in tags:
    print(item.text, end=' ')
print()
