from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wdWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome()
WAIT = wdWait(browser, 10)
browser.get('https://www.bilibili.com/')

# 解决自动化执行浏览器窗口太小导致页面元素不可见报错问题
js = "document.getElementsByClassName('nav-search-box')[0].style.display='block'"
# 执行js代码
browser.execute_script(js)

input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#nav_searchform > input')))
submit = WAIT.until(EC.element_to_be_clickable((By.XPATH, '//form[@id="nav_searchform"]//button')))

input.send_keys('蔡徐坤 篮球')
submit.click()

print('跳转到新窗口')
all_h = browser.window_handles
browser.switch_to.window(all_h[1])
total = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#server-search-app > div.contain > div.body-contain > div > div.page-wrap > div > ul > li.page-item.last > button')))
for i in range(2, int(total + 1)):
    next_page(i)

def next_page(page_num):
    print('获取下一页数据')
    try:
        next_btn = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#server-search-app > div.contain > div.body-contain > div > div.page-wrap > div > ul > li.page-item.next > button')))
        next_btn.click()
        WAIT.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#server-search-app > div.contain > div.body-contain > div > div.page-wrap > div > ul > li.page-item.active > button'), str(page_num)))
    except TimeoutException:
        browser.refresh()
        return next_page(page_num) 


def get_source():
    print(21111)

    
