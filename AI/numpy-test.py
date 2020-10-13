import numpy as np
arr = np.array([1,2,3,4,5])
print(type(arr)) # <class 'numpy.ndarray'>
arr2 = arr + 1 
print(arr2) # [2 3 4 5 6]
print(arr+arr2) # [ 3  5  7  9 11]
print(arr * arr2) # [ 2  6 12 20 30]
print(arr) # [1 2 3 4 5]
print(arr.shape) # (5,) 输出结果表示当前数组为一维数组，有5个元素

#target_list = [1,2,3,4,5]
#target_list.shape() 普通数组无法使用shape函数

#二维数组
np.array([[1,2,3], [4,5,6]]) # array([[1, 2, 3], [4, 5, 6]])

#numpy.array数组类型自动向下转换(int->float->str)
test_array = np.array([1,2,3,4,'5']);
print(test_array) # ['1' '2' '3' '4' '5']
test_array1 = np.array([1,2,3,4,5.0]);
print(test_array1) # [1. 2. 3. 4. 5.]

#numpy属性操作
print(type(arr)) # numpy.ndarray
print(arr.dtype) # int32
print(arr.size) # 5
print(arr.ndim) # 1：维度，一维

#切割和索引
print(arr[1:3]) # [2 3]
print(arr[-2:]) # [4 5]
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2[1,1] = 10 
print(arr2) # [[ 1  2  3] [ 4 10  6] [ 7  8  9]]
# 取二维数组某列全部数据
print(arr2[:,1]) # [ 2 10  8],却二维数组下标为1列的所有数据，“:”表示全部列

#bool索引
bool_arr = np.arange(0,100,10) # [0,10,20,30,40,50,60,70,80,90]从0到100， 每隔10取一个元素
bool_mask = np.array([0,0,0,1,1,1,0,0,1,1], dtype=bool) # [False,False,False,True,True,False,False,True,True]
print(bool_arr[bool_mask]) # [30 40 50 80 90]，过滤出值为True对应的下标的bool_arr元素
bool_arr1 = np.random.rand(10) # 生成10个(0,1)之间的随机数
print(bool_arr1) # [0.74400221 0.83496011 0.81091883 0.62413278 0.7731349  0.86001773 0.76385504 0.21132968 0.35685337 0.4047908 ]
bool_mask1 = bool_arr1 > 0.5
print(bool_mask1) # [ True  True  True  True  True  True  True False False False]
print(np.where(bool_arr>30)) # (array([4, 5, 6, 7, 8, 9] dtype=int64),) 获取符合条件下标
print(bool_arr[np.where(bool_arr>30)]) # [40 50 60 70 80 90] 获取符合条件元素
x = np.array([1,1,1,5])
y = np.array([1,1,1,0])
print(x == y) # array([ True,  True,  True, False])
print(np.logical_and(x, y)) # 逻辑与 True  True  True  True]
print(np.logical_or(x, y)) # 逻辑或，[ True  True  True  True]

