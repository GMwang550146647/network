from bs4 import BeautifulSoup

with open('3.html') as f:
    html = f.read()
    soup = BeautifulSoup(html)
    # 1.根据属性、标签查找
    print(soup.find('div', id='divSearchPanel'))
    print(soup.find('ul', class_='d1 ico3'))
    print(soup.find_all('ul', class_='d1 ico3'))
    # 2.根据位置查找
    pos1=soup.select('body > div:nth-child(1) > div.navbar > ul')
    print(pos1)
    pos2=soup.select('#divSearchPanel')
    print(pos2)
