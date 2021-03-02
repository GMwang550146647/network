from selenium.common.exceptions import TimeoutException
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
"""
0.设置浏览器不可见
"""
# option = webdriver.ChromeOptions()
# option.add_argument('headless')  # 设置option
driver = webdriver.Chrome(executable_path='driver/chromedriver')  # 调用带参数的谷歌浏览器
"""
1.打开浏览器并输入网址浏览
"""

url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
driver.get(url)
# 跳到iframe中
iframe = driver.find_elements_by_tag_name('iframe')[0]
driver.switch_to.frame(iframe)
div_tag = driver.find_element_by_id('draggable')
action=ActionChains(driver)
action.click_and_hold(div_tag)
for i in range(5):
    action.move_by_offset(17,5).perform()
    time.sleep(0.4)