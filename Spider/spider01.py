from urllib import request,parse
import ssl

# response = request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

context = ssl._create_unverified_context()
headers = {
    'Content-Type': 'application/json',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
dict = {
    'return_url':'https://127.0.0.1',
    'user_name':'test',
    'password':'test'
}
data = bytes(parse.urlencode(dict), 'utf-8')
req = request.Request('https://https://127.0.0.1/login', data=data, headers=headers, method='POST')
response = request.urlopen(req, context=context)
print(response.read().decode('utf-8'))
