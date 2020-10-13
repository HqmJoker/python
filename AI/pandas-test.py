import pandas as pd # 引入数据分析处理库pandas
# (读取结果对象属性参考文档)https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
df = pd.read_csv('./train.csv')

df.head() # 展示读取数据，默认前5条
#df.head(10) # 展示读取数据前10条
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

#iloc函数相关
df.iloc[0] # 获取第1行数据(非表头)
df.iloc[:5] # 获取前5行数据(非表头)
df.iloc[:5,1:4] # 获取前5行数据,[1:4]:获取1,2,3列的字段数据（默认从第0列开始）
#loc函数相关
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

#自定义DataFrame数据
data = {'country':['China', 'America', 'India'],
       'population':[14, 3, 12]}
df_data = pd.DataFrame(data)
print(df_data)

#pandas配置对象
pd.get_option('display.max_rows')
pd.set_option('display.max_rows', 6)
#pd.Series(index = range(0,100)) # Series相当二维数据中某一行或一列
pd.get_option('display.max_columns')