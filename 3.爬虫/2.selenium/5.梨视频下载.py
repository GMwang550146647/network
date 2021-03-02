from selenium import webdriver
import time
"""
0.设置浏览器不可见
"""
option = webdriver.ChromeOptions()
option.add_argument('headless')  # 设置option
option.add_argument('disable-gpu')  # 设置option
driver = webdriver.Chrome(executable_path='driver/chromedriver',options=option)  # 调用带参数的谷歌浏览器
# driver = webdriver.Chrome(executable_path='driver/chromedriver')  # 调用带参数的谷歌浏览器

url='https://www.pearvideo.com/category_8'
driver.get(url)
for i in range(30):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(0.2)
news_tags=driver.find_elements_by_xpath('//*[@id="categoryList"]/li')
urls=[]
for news_tag_i in news_tags:
    url_i=news_tag_i.find_element_by_class_name('vervideo-lilink').get_attribute('href')
    urls.append(url_i)
with open('5.video_urls.csv','w') as f:
    f.write('\n'.join(urls))
