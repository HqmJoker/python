# 进程、线程相关
'''
# v1.0（进程）
import time

def moyu_time(name, delay, counter):
    while counter:
        time.sleep(delay)
        print('%s 开始测试 %s' %(name, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
        counter -= 1
if __name__ == '__main__':
    moyu_time('test', 1, 10)
'''
'''
# v2.0（线程）
import threading
import time

# 创建一个线程子类
class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print('线程开始：' + self.name)
        moyu_time(self.name, self.counter, 5)
        print('退出线程：' + self.name)
def moyu_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print('%s 开始测试 %s'%(threadName, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
        counter -= 1
if __name__ == '__main__':
    thread1 = MyThread(1, 'test1', 1)
    thread2 = MyThread(2, 'xiaoming', 2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print('退出主线程')
'''
'''
#  v3.0（线程池）
import time
from concurrent.futures import ThreadPoolExecutor

def moyu_time(name, delay, counter):
    while counter:
        time.sleep(delay)
        print('%s 开始测试 %s' %(name, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
        counter -= 1

if __name__ == '__main__':
    pool = ThreadPoolExecutor(20) # 创建一个大小为20的线程池
    for i in range(1,5):
        pool.submit(moyu_time('test'+str(i), 1, 5))
'''
# v4.0（使用线程队列创建线程池）
from queue import Queue 
import threading
import time

class CustomThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.__queue = queue
    def run(self):
        while True:
            q_method = self.__queue.get()
            q_method()
            self.__queue.task_done()

def moyu():
    print(' 开始测试 %s' %(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))

if __name__ == '__main__':
    queue = Queue(5)
    for i in range(queue.maxsize):
        t = CustomThread(queue)
        t.setDaemon(True)
        t.start()
    for i in range(1, 20):
        queue.put(moyu)
    queue.join()