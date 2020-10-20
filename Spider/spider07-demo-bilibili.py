from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wdWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup 
import xlwt

# 下一页函数
def next_page(page_num):
    print('获取第 %d 页数据'%(page_num))
    get_source()
    next_btn = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#server-search-app #all-list ul.pages > li.next > button')))
    next_btn.click()
    WAIT.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#server-search-app #all-list ul.pages > li.active > button'), str(page_num+1)))
# 获取资源函数
def get_source():
    WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#server-search-app > div.contain > div.body-contain > div ul.video-list')))
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    save_to_excel(soup)
# 保存为excek文件
def save_to_excel(soup):
    list = soup.find(class_='video-list').find_all(class_='video-item')

    for item in list:
        item_title = item.find('a').get('title')
        item_link = item.find('a').get('href')
        item_dec = item.find(class_='des hide').text
        item_view = item.find(class_='so-icon watch-num').text
        item_danmu = item.find(class_='so-icon hide').text
        item_date = item.find(class_='so-icon time').text
        print('爬取：' + item_title)

        global n 
        sheet.write(n, 0, item_title)
        sheet.write(n, 1, item_link)
        sheet.write(n, 2, item_dec)
        sheet.write(n, 3, item_view)
        sheet.write(n, 4, item_danmu)
        sheet.write(n, 5, item_date)
        n = n + 1

# browser = webdriver.Chrome()
browser = webdriver.PhantomJS()
WAIT = wdWait(browser, 10)
browser.get('https://www.bilibili.com/')

# 解决自动化执行浏览器窗口太小导致页面元素不可见报错问题
js = "document.getElementsByClassName('nav-search-box')[0].style.display='block'"
# 执行js代码
browser.execute_script(js)
# browser.set_window_size(1400, 900) 同样解决浏览器窗口太小导致元素不可见问题

# 创建excel工作空间
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('b站蔡徐坤打篮球视频列表', cell_overwrite_ok=True)
sheet.write(0, 0, '标题')
sheet.write(0, 1, '链接')
sheet.write(0, 2, '描述')
sheet.write(0, 3, '观看次数')
sheet.write(0, 4, '弹幕')
sheet.write(0, 5, '日期')
n = 1

# 关键字搜索
input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#nav_searchform > input')))
submit = WAIT.until(EC.element_to_be_clickable((By.XPATH, '//form[@id="nav_searchform"]//button')))
input.send_keys('蔡徐坤 篮球')
submit.click()
# 打开并切换到新窗口
all_h = browser.window_handles
browser.switch_to.window(all_h[1])
total = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#server-search-app #all-list ul.pages > li.page-item.last > button')))

# 循环遍历页码，获取所有页面视频
try:
    for i in range(1, int(total.text) + 1):
        next_page(i)
except TimeoutException:
    print('超时')
    # browser.refresh()
    # next_page(i) 
finally:
    book.save(u'蔡徐坤篮球.xls')
    print('结束')
    # browser.close()
    
