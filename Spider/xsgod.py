import requests
from bs4 import BeautifulSoup
import time

baseUrl = 'http://www.xsgod.com'

# 根据传入url获取html
def getHtml(url):
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
  }
  response = requests.get(url, headers=headers)
  time.sleep(2)
  if response.status_code == 200:
    return response.text
  else:
    print('error:', response)

# 查找出对应链接
def getPageLink(soup):
  formatData = soup.find(class_='booklist').find_all('li')
  textLinkList = []
  for item in formatData:
    url = item.find('a').get('href')
    textLinkList.append(baseUrl + url)
  return textLinkList

# 保存成txt文件
def save_to_text():
  pass

if __name__ == '__main__':
  url = baseUrl + '/Html/Book/89/89300/1/'
  html = getHtml(url)
  soup = BeautifulSoup(html, 'lxml')
  textLink = getPageLink(soup)

  print(textLink[0])
  pageDetailHtml = getHtml(textLink[0])
  pageDetailSoup = BeautifulSoup(pageDetailHtml, 'lxml')

  print(pageDetailSoup)
