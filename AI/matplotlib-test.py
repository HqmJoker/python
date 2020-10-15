import numpy as np
import matplotlib.pyplot as plt # 引入绘图相关函数
# 在jupyter中console显示图
%matplotlib inline 

# 常规绘图
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25]) # 生成图表
plt.xlabel('xlabel', fontsize = 16) # 设置x轴标签
plt.ylabel('ylabel') # 设置y轴标签
plt.cla() # 清空画布
#  '-.' ： 虚点线
# 多次调用plt.plot()图像会叠加
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], '-.', color = 'r')
plt.xlabel('xlabel', fontsize = 16)
plt.ylabel('ylabel')
plt.cla() # 清空画布
he_array = np.arange(0, 10, 0.5)
plt.plot(he_array, he_array, 'r--')
plt.plot(he_array, he_array**2, 'bs')
plt.plot(he_array, he_array**3, 'go')
plt.cla() # 清空画布
x = np.linspace(-10, 10)
y = np.sin(x)
plt.plot(x, y, linewidth = 3.0)
plt.cla() # 清空画布
plt.plot(x, y, color='b', linestyle=':', marker='o', markerfacecolor='r', markersize=10) # color:线颜色,linestyle:线条类型,marker:点标记
plt.cla() # 清空画布
line = plt.plot(x, y) 
plt.setp(line, color='r', linewidth=2.0, alpha=0.1) # alpha透明度
plt.cla() # 清空画布
# 211：2行一列子图中的第一个子图，212：2行一列子图中的第二个子图
plt.subplot(211)
plt.plot(x, y, color='r')
plt.subplot(212)
plt.plot(x, y, color='b')
# 121：一行2列子图中的第一个子图，112：一行2列子图中的第二个子图
plt.subplot(121)
plt.plot(x, y, color='r')
plt.subplot(122)
plt.plot(x, y, color='b')
plt.cla() # 清空画布

plt.subplot(321)
plt.plot(x, y, color='r')
plt.subplot(326)
plt.plot(x, y, color='b')
