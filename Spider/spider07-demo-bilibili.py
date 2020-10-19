from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wdWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
WAIT = wdWait(browser, 10)
browser.get('https://www.bilibili.com/')

# 解决自动化执行浏览器窗口太小导致页面元素不可见报错问题
js = "document.getElementsByClassName('nav-search-box')[0].style.display='block'"
# 执行js代码
browser.execute_script(js)

input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#nav_searchform > input')))
submit = WAIT.until(EC.element_to_be_clickable((By.XPATH, '//form[@id="nav_searchform"]//button')))
# submit = WAIT.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav_searchform"]//div[@class="nav-search-btn"]//button')))
# submit = WAIT.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div/div[2]/div/form/div/button')))

input.send_keys('蔡徐坤 篮球')
submit.click()