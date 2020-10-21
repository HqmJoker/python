'''
# 多进程 v1.0 直接创建进程
from multiprocessing import Process

def f(name):
    print('hello:', name)

if __name__ == '__main__':
    p = Process(target=f, args=('test',))
    p.start()
    p.join()
'''
# 多进程 v2.0 通过进程池方式创建进程
from multiprocessing import Pool

def f(x):
    return x*x
if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1,2,3]))