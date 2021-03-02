"""
1.特点：
    慢，但是可见即可用
2.安装：
    安装python接口 ：  pip install selenium
    下载 chrome浏览器接口：https://chromedriver.chromium.org/downloads
"""
import time
from selenium import webdriver
from PIL import Image
"""
1.打开浏览器并输入网址
"""
driver = webdriver.Chrome(executable_path='driver/chromedriver')
# driver=webdriver.Firefox(executable_path='driver/geckodriver')
# driver = webdriver.Safari(executable_path='/usr/bin/safaridriver')  # Develop -> Allow Remote Automation
driver.get('http://www.cdcer.net/jx/')

# 设置超时时间
driver.set_page_load_timeout(5)
driver.set_script_timeout(5)  # 这两种设置都进行才有效
"""
2.去掉弹框
"""
time.sleep(1)
a = driver.switch_to.alert
a.accept()

"""
2.操作html 内容
"""
# 1.填写 input
video_input = driver.find_element_by_xpath('//*[@id="valueurl"]')
video_input.send_keys('https://www.iqiyi.com/v_1ihkivfj14k.html?vfm=2008_aldbd&fv=p_02_01')
time.sleep(1)

# 2.按键
btn = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/input[1]')
for i in range(2):
    btn.click()
    time.sleep(1)

# 3.转换到其他地方
iframe = driver.find_elements_by_tag_name('iframe')[0]
print(iframe)
driver.switch_to.frame(iframe)
time.sleep(1)
video_url = driver.find_element_by_xpath('//*[@id="a1"]/div[2]/video')
print(video_url.value_of_css_property('src'))

# 4.拖动页面
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
