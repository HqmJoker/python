import requests
import re
import json

# 获取第几页数据
def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = requests_dandan(url)
    items = parse_result(html)
    for item in items:
        write_item_to_file(item)
# 请求数据函数
def requests_dandan(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None
# 过滤出需要的数据
def parse_result(html):
    pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'range':item[0],
            'image':item[1],
            'title':item[2],
            'recommend':item[3],
            'author':item[4],
            'times':item[5],
            'price':item[6]
        }
# 保存格式化数据到本地文本
def write_item_to_file(item):
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()

for i in range(1, 5):
    main(i)