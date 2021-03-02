from selenium.common.exceptions import TimeoutException
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_goods(url, driver):
    try:
        driver.get(url)
    except TimeoutException as err:
        print(err)

    for i in range(6):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(0.2)
    next_page_btn = driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[9]')
    page_source=driver.page_source
    goods=driver.find_elements_by_xpath("""//*[@id="J_goodsList"]/ul/li""")
    goods_list = [good_i.text.split('\n') for good_i in goods]
    return goods_list



"""
0.设置浏览器不可见
"""
option=webdriver.ChromeOptions()
option.add_argument('headless') # 设置option
driver = webdriver.Chrome(chrome_options=option,executable_path='../driver/chromedriver')  # 调用带参数的谷歌浏览器

"""
1.打开浏览器并输入网址
"""
# 设置超时时间
driver.set_page_load_timeout(3)
driver.set_script_timeout(3)  # 这两种设置都进行才有效

"""
2.操作html 内容
"""
all_goods = []
url = 'https://list.jd.com/list.html?cat=1318%2C12099%2C9754&page={}&s=1&click=0'
for i in range(6):
    goods = get_goods(url.format(i+1), driver)
    all_goods.extend(goods)
with open("2.data.csv",'w') as f:
    f.write('\n'.join(['\t'.join(good_i) for good_i in all_goods]))