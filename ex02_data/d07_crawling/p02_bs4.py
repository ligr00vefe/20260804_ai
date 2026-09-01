import bs4

webPage = open('./Sample02.html', 'rt', encoding='utf-8').read()
bsObj = bs4.BeautifulSoup(webPage, 'html.parser')

tag_div = bsObj.find('div')
print(tag_div)

ul_div = bsObj.find('ul')
print(ul_div)

ul_div = bsObj.find('li')
print(ul_div)

ul_div = bsObj.find_all('li')
print("ul_div: ", ul_div)

webPage = open('./Sample03.html', 'rt', encoding='utf-8').read()
bsObj = bs4.BeautifulSoup(webPage, 'html.parser')

tag = bsObj.find('div', {'id': 'myId1'})
print(tag)
tag = bsObj.find('div', {'class': 'myClass1'})
print("tag.text: ", tag.text)
tags = bsObj.find_all('div', {'class': 'myClass1'})
for t in tags:
    print(t.text)
tags = bsObj.find_all('a')

for t in tags:
    print(t['href'], t.text)

for i in range(len(tags)):
    print((tags[i])['href'], tags[i].text)
