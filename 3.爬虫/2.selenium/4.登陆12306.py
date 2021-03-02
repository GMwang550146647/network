from selenium.common.exceptions import TimeoutException
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from PIL import Image
import requests
from urllib.request import urlretrieve
def download_photo(img_url,file_name):
    urlretrieve(img_url, file_name)
    # content=requests.get(img_url).content
    # with open(file_name,'w') as f:
    #     f.write(content)
"""
0.设置浏览器不可见
"""
option = webdriver.ChromeOptions()
option.add_argument('headless')  # 设置option
option.add_argument('disable-gpu')  # 设置option
driver = webdriver.Chrome(executable_path='driver/chromedriver',options=option)  # 调用带参数的谷歌浏览器
# driver = webdriver.Chrome(executable_path='driver/chromedriver')  # 调用带参数的谷歌浏览器
driver.maximize_window()
"""
1.打开浏览器并输入网址浏览
"""

url = 'https://kyfw.12306.cn/otn/resources/login.html'
driver.get(url)
time.sleep(0.1)
login_tag=driver.find_element_by_class_name('login-hd-account')
login_tag.click()
time.sleep(0.1)
driver.save_screenshot('4.main_page.png')
time.sleep(0.1)
image_tag=driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[3]/div/div[4]/img')[0]
location=image_tag.location
size=image_tag.size
rectangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y'])+size['height'])
download_photo(image_tag.get_attribute('src'),"4.check_code.png")
