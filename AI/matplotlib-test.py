import math 
import numpy as np
import matplotlib.pyplot as plt # 引入绘图相关函数
# 在jupyter中console显示图
%matplotlib inline 

# 常规绘图
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25]) # 生成图表
plt.xlabel('xlabel', fontsize = 16) # 设置x轴标签
plt.ylabel('ylabel') # 设置y轴标签
plt.clf() # 清空画布
#  '-.' ： 虚点线
# 多次调用plt.plot()图像会叠加
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], '-.', color = 'r')
plt.xlabel('xlabel', fontsize = 16)
plt.ylabel('ylabel')
plt.clf() # 清空画布
he_array = np.arange(0, 10, 0.5)
plt.plot(he_array, he_array, 'r--')
plt.plot(he_array, he_array**2, 'bs')
plt.plot(he_array, he_array**3, 'go')
plt.clf() # 清空画布
x = np.linspace(-10, 10)
y = np.sin(x)
plt.plot(x, y, linewidth = 3.0)
plt.clf() # 清空画布
plt.plot(x, y, color='b', linestyle=':', marker='o', markerfacecolor='r', markersize=10) # color:线颜色,linestyle:线条类型,marker:点标记
plt.clf() # 清空画布
line = plt.plot(x, y) 
plt.setp(line, color='r', linewidth=2.0, alpha=0.1) # alpha透明度
plt.clf() # 清空画布
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
plt.clf() # 清空画布
plt.subplot(321)
plt.plot(x, y, color='r')
plt.subplot(326)
plt.plot(x, y, color='b')
plt.clf() # 清空画布
# 增加标注
plt.plot(x, y, color='b', linestyle=':', marker='o', markerfacecolor='r', markersize=10)
plt.xlabel('x:---')
plt.ylabel('y:---')
plt.title('he qin ming:---') # 图表标题
plt.text(0, 0, 'he qin ming') # 在指定位置显示文字
plt.grid(True) # 显示网格
plt.annotate('heqinming', xy=(-5,-0.75), xytext=(-2,-0.25), arrowprops=dict(facecolor='red', shrink=0.05, headlength=20, headwidth=20)) # 添加箭头
plt.clf() # 清空画布
x1 = range(10)
y1 = range(10)
fig = plt.gca() # 获取当前图表对象
plt.plot(x1, y1)
fig.axes.get_xaxis().set_visible(False) # 清空x轴坐标
fig.axes.get_yaxis().set_visible(False) # 清空y轴坐标
plt.clf() # 清空画布
'''
loc：float
    此概率分布的均值（对应着整个分布的中心centre）
scale：float
    此概率分布的标准差（对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高）
size：int or tuple of ints
    输出的shape，默认为None，只输出一个值
'''
x2 = np.random.normal(loc = 0.0, scale = 1.0, size = 300) # 生成高斯分布的概率密度随机数
width = 0.5
bins = np.arange(math.floor(x.min()) - width, math.ceil(x.max())+width, width) # 每隔0.5生成横坐标
ax = plt.subplot(111) # 绘制图表
ax.spines['top'].set_visible(False) # 去掉上边线
ax.spines['right'].set_visible(False) # 去掉右边线
plt.tick_params(bottom=False, top=False, left=True, right=False) # 隐藏坐标轴刻度线
plt.grid() # 加入网格线
plt.hist(x2, alpha=0.5, bins=bins) # 绘制直方图
