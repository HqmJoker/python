import pandas as pd # 引入数据分析处理库pandas
import numpy as np
# (读取结果对象属性参考文档)https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
df = pd.read_csv('./train.csv')

df.head() # 展示读取数据，默认前5条
# df.head(10) # 展示读取数据前10条
df.tail() # 展示读取数据，默认后5条
df.info() # 读取csv文件返回结果默认数据格式
df.index # RangeIndex(start=0, stop=891, step=1)读取csv文件返回结果索引相关信息
df.columns # 返回数据列名称 Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],dtype='object')
df.dtypes # 返回数据列对应的类型，object表示python的字符串(str)
df.values # 获取返回结果数据矩阵

age = df['Age']
age[:5] # 获取Age列前5个数据[:5]为list[0:5]
age.values[:5] # array([22., 38., 26., 35., 35.])

df = df.set_index('Name') # 默认从0开始自增，自定义索引后更新为定义的索引
df.head()

age1 = df['Age']
age1['Allen, Mr. William Henry']

df = df.reset_index() # 重置索引
df[['Age', 'Fare']][:5]

# iloc函数相关
df.iloc[0] # 获取第1行数据(非表头)
df.iloc[:5] # 获取前5行数据(非表头)
df.iloc[:5,1:4] # 获取前5行数据,[1:4]:获取1,2,3列的字段数据（默认从第0列开始）
# loc函数相关
df = df.set_index('Name')
df.loc['Heikkinen, Miss. Laina'] # 获取对应索引的行信息
df.loc['Heikkinen, Miss. Laina', 'Fare'] # 获取对应索引的行指定字段信息
df.loc[['Heikkinen, Miss. Laina', 'Allen, Mr. William Henry']] # 获取多个索引的行指定字段信息
df.loc['Heikkinen, Miss. Laina':'Allen, Mr. William Henry'] # 获取多个索引的区间的行指定字段信息

df['Fare']>40 # 显示票价大于40
df[df['Fare']>40][:5] # 显示票价大于40的前5条数据
df[df['Sex'] == 'male'][:5] # 男性的前5条数据
df.loc[df['Sex'] == 'male', 'Age'].mean() # 找到所有男性的平均年龄
(df['Age']>70).sum() # 计算年龄大于70的乘客的总数

# 自定义DataFrame数据
data = {'country':['China', 'America', 'India'],
       'population':[14, 3, 12]}
df_data = pd.DataFrame(data)

# pandas配置对象
pd.get_option('display.max_rows')
pd.set_option('display.max_rows', 10)
# pd.Series(index = range(0,100)) # Series相当二维数据中某一行或一列
pd.get_option('display.max_columns')

# danpas.DataTarget对象的相关统计指标
df.describe() # 数量，均值，标准差，最小值，最大值
df.cov() # 协方差矩阵
df.corr() # 相关系数
df['Sex'].value_counts() # 统计性别列所有属性数据
df['Sex'].value_counts(ascending = True) # 统计性别列所有属性数据，数据少的先显示
df['Age'].value_counts(ascending = True) # 统计年龄列所有属性数据，数据少的先显示
df['Age'].value_counts(ascending = True, bins = 5) # 统计年龄列所有属性数据，平均分成5组，数据少的先显示

# 数据透视表
# 测试数据
testData = pd.DataFrame({'Month':['January', 'January', 'January', 'January',
                                   'February', 'February', 'February', 'February',
                                   'March', 'March', 'March', 'March'],
                          'Categories':['Transportation', 'Grocery', 'HouseHold', 'Entertainment',
                                       'Transportation', 'Grocery', 'HouseHold', 'Entertainment',
                                       'Transportation', 'Grocery', 'HouseHold', 'Entertainment'],
                          'Amount':[74., 235., 175., 100., 115., 240., 225., 125., 90., 26., 200., 120.]
                         })
test_pivot = testData.pivot(index = 'Categories', columns='Month', values='Amount') # 统计每个月花费在各项用途上的金额分别是多少
test_pivot.sum(axis = 1) # 统计这几个月每个类型花费总金额
test_pivot.sum()# 统计每个月花费总金额
df.pivot_table(index='Sex', columns='Pclass', values='Fare') # 按乘客性别分别统计各个舱位(Pclass)购票的平均价格
df.pivot_table(index='Sex', columns='Pclass', values='Fare', aggfunc='max') # 按乘客性别分别统计各个舱位(Pclass)购票的最高价格
df.pivot_table(index='Sex', columns='Pclass', values='Fare', aggfunc='count') # 按乘客性别分别统计各个舱位(Pclass)购票的人数
#统计未成年和成年人不同性别的平局获救可能性
df['Underaged'] = df['Age'] <= 18
df.pivot_table(index='Underaged', columns='Sex', values='Survived')

# groupby 操作
gb = pd.DataFrame({
    'key':['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'data':[0, 5, 10, 5, 10, 15, 10, 15, 20]
})
# 求 A,B,C的总和
for key in ['A', 'B', 'C']:
    print(key, gb[gb['key']==key].sum())
gb.groupby('key').sum()
# 求 A,B,C的均值
gb.groupby('key').aggregate(np.mean)

# 求船上不同性别的平均年龄
df.groupby('Sex')['Age'].mean()
df.pivot_table(index='Sex', values='Age')

gb_test = pd.DataFrame({
    'A':['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B':['one','one','two','three','two','two','one','three'],
    'C':np.random.randn(8),
    'D':np.random.randn(8)
})
gb_test.groupby('A').count() # 统计A的groupby对应的数量
gb_test['A'].value_counts() # 统计A的groupby对应的数量
gb_test.groupby(['A','B']).count()# 统计多列的groupby对应的数量
gb_test.groupby(['A','B']).sum()# 统计多列的groupby总和
gb_test.groupby(['A','B']).aggregate(np.mean)# 统计多列的groupby均值

# Merge on:合并关键字 how：以何种方式合并（左连接/右连接）
left = pd.DataFrame({
    'key':['K0', 'K1', 'K2', 'K3'],
    'A':['A0', 'A1', 'A2', 'A3'],
    'B':['B0', 'B1', 'B2', 'B3']
})
right = pd.DataFrame({
    'key':['K0', 'K1', 'K2', 'K3'],
    'C':['C0', 'C1', 'C2', 'C3'],
    'D':['D0', 'D1', 'D2', 'D3']
})
res = pd.merge(left, right, on = 'key')
# 排序操作
data = pd.DataFrame({
    'group':['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'],
    'data':[4, 3, 2, 1, 12, 3, 4, 5, 7]
})
data.sort_values(by=['group', 'data'], ascending=[False, True], inplace=True)
# 缺失值处理
data1 = pd.DataFrame({
    'k1':['one']*3+['two']*4,
    'k2':[3, 2, 1, 3, 3, 4, 4]
})
print(data1.drop_duplicates()) # 移除重复数据
print(data1.drop_duplicates(subset='k1')) # 移除k1列重复数据
data2 = data1.assign(k3 = data1['k2']+1) # 添加列
print(data2) 

# 统计每一列空值个数
def nan_count(series):
    columns_null = pd.isnull(series)
    null = series[columns_null]
    return len(null)
columns_null_count = df.apply(nan_count)
print(columns_null_count)
# 判断每一行是否为成年人
def is_minor(series):
    if(series['Age']<18):
        return True
    else:
        return False
row_is_minor = df.apply(is_minor, axis=1)
print(row_is_minor)

# 时间操作
ts = pd.Timestamp('2020-10-14') # 2020-10-14 00:00:00
ts.month # 10
ts.day # 14
ts + pd.Timedelta('5 days') # Timestamp('2020-10-19 00:00:00')

s = pd.Series(['2020-10-14 00:00:00', '2020-10-15 00:00:00', '2020-10-16 00:00:00'])
ts1 = pd.to_datetime(s)
print(ts1)
ts1.dt.hour # 输出列表对应小时
ts1.dt.weekday # 输出列表对应星期几，默认从0开始，即0对应星期一
pd.Series(pd.date_range(start='2020-10-14', periods=10, freq='12H')) # 从start(2020-10-14)开始生成periods(10)条数据，每条数据相隔freq(12H)

# 绘图操作
%matplotlib inline
df_paint = pd.DataFrame(
    np.random.randn(10, 4).cumsum(0),
    index = np.arange(0 ,100, 10),
    columns = ['A', 'B', 'C', 'D']
)
print(df_paint)
df_paint.plot() # 绘制图标
import matplotlib.pyplot as plt
fig, axes = plt.subplots(2, 1) # 创建子图2行一列的形式, fig参数不可删除（删除后会报错：https://blog.csdn.net/xavier_muse/article/details/83859272）
data_paint = pd.Series(np.random.rand(16), index = list('abcdefghijklmnop'))
data_paint.plot(ax = axes[0], kind = 'bar') # 绘制第一个子图，axes[0]为第一个子图
data_paint.plot(ax = axes[1], kind = 'barh') # 绘制第二个子图，axes[1]为第二个子图
# 绘制多条形图
df_paint1 = pd.DataFrame(np.random.rand(6, 4), index = ['one', 'two', 'three', 'four', 'five', 'six'],
                         columns = pd.Index(['A', 'B', 'C', 'D'], name = 'Genus'))
df_paint1.plot(kind = 'bar')

# 大数据处理技巧
gl = pd.read_csv('./game_logs.csv')
gl.head()
print(gl.shape) # 输出样本数据行、列数(26265, 161)
gl.info(memory_usage = 'deep') # memory = deep表示要详细地展示当前数据占用的内存 dtypes: float64(85), int64(3), object(73) memory usage: 94.0 MB
# 计算各种数据类型平均占用内存
for dtype in ['float64', 'int64', 'object']:
    selected_dtype = gl.select_dtypes(include = [dtype])
    mean_usage_b = selected_dtype.memory_usage(deep = True).mean()
    mean_usage_mb = mean_usage_b/1024**2 # 转换为MB, 等同于mean_usage_b/1024/1024
    print('平均内存占用', dtype, mean_usage_mb)
# 把int64数据类型转换成int32
def mem_usage(pandas_obj):
    if isinstance(pandas_obj, pd.DataFrame): # 如果参数padans_obj是pd.DataFrame的实例，或者padans_obj是pd.DataFrame类的子类的一个实例， 返回True。
        usage_b = pandas_obj.memory_usage(deep = True).sum()
    else:
        usage_b = pandas_obj.memory_usage(deep = True)
    usage_mb = usage_b/1024**2
    return '{:3.2f} MB'.format(usage_mb) # 表示三位数，其中2位为小数 格式化输出 "{0:H^20.3f}".format(12345.67890)->'HHHHH12345.679HHHHHH'

# 大数据量 int64 向下类型转换内存占用情况
gl_int = gl.select_dtypes(include = ['int64'])
coverted_int = gl_int.apply(pd.to_numeric, downcast = 'integer') # downcast = 'integer'自动向下类型转换
print(mem_usage(gl_int))
print(mem_usage(coverted_int))
# 大数据量 float64 向下类型转换内存占用情况
gl_float = gl.select_dtypes(include = ['float64'])
coverted_float = gl_float.apply(pd.to_numeric, downcast = 'float') # downcast = 'float'自动向下类型转换
print(mem_usage(gl_float))
print(mem_usage(coverted_float))
# object(字符串)类型
gl_obj = gl.select_dtypes(include = ['object']).copy()
gl_obj.describe()
dow = gl_obj.day_of_week
dow_cat = dow.astype('category')
dow_cat.head()
dow_cat.head(10).cat.codes
print(mem_usage(dow))
print(mem_usage(dow_cat))
# 大数据量 object 向下类型转换内存占用情况
converted_obj = pd.DataFrame()
for col in gl_obj.columns:
    num_unique_values = len(gl_obj[col].unique())
    num_total_values = len(gl_obj[col])
    if num_unique_values / num_total_values < 0.5:
        converted_obj.loc[:,col] = gl_obj[col].astype('category')
    else:
        converted_obj.loc[:,col] = gl_obj[col]
print(mem_usage(gl_obj))
print(mem_usage(converted_obj))
