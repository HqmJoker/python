from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')

def hello_world():
    print(request.headers)
    if(str(request.headers.get('User-Agent')).startswith('python')):
        return '错误返回结果：这里做过滤掉python的爬虫'
    else:
        return '正确返回结果：假设这里是数据'
        

if __name__ == '__main__':
    app.run(debug=True)