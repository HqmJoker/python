import numpy as np
arr = np.array([1,2,3,4,5])
print(type(arr))
arr2 = arr + 1
print(arr2)
print(arr+arr2)
print(arr * arr2)
print(arr)
print(arr.shape) #输出结果表示当前数组为一维数组，有5个元素

#target_list = [1,2,3,4,5]
#target_list.shape() 普通数组无法使用shape函数

#二维数组
np.array([[1,2,3], [4,5,6]])

#numpy.array数组类型自动向下转换(int->float->str)
test_array = np.array([1,2,3,4,'5']);
print(test_array) # ['1' '2' '3' '4' '5']
test_array1 = np.array([1,2,3,4,5.0]);
print(test_array1) # [1. 2. 3. 4. 5.]
