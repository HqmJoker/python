import requests
# r = requests.get('https://api.github.com/events')
# r = requests.get('https://api.github.com/events', params={'key':'value'})
r = requests.post('https://httpbin.org/post', headers={'user-agent': 'my-app/0.0.1'}, data = {'key':'value'})
print(r)
print(r.text) # 获取服务器响应文本内容
print(r.status_code) # 获取响应码
print(r.headers) # 获取响应头
print(r.json()) # 获取 Json 响应内容
# 获取 socket 流响应内容
print(r.raw)
print(r.raw.read(10))
print(r.content) # 获取字节响应内容
