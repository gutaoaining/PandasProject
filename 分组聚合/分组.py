# 作者：顾涛
# 创建时间：2025/6/15
import numpy as np
import pandas as pd

# 准备数据
df = pd.DataFrame(data={'sex': np.random.randint(0, 2, size=300),  # 0 男，1女
                        'class': np.random.randint(1, 9, size=300),  # 1-8八个班
                        'Python': np.random.randint(0, 151, size=300),  # Python成绩
                        'Keras': np.random.randint(0, 151, size=300),  # Keras成绩
                        'Tensorflow': np.random.randint(0, 151, size=300),
                        'Java': np.random.randint(0, 151, size=300),
                        'C++': np.random.randint(0, 151, size=300)})
print(f'原始数据：\n{df}')
df['sex'] = df['sex'].map({0: '男', 1: '女'})  # 将0，1映射成男女
# 1、分组-> 可迭代对象
# 1.1先分组再获取数据
print(f'映射性别后的数据：\n{df}')
g = df.groupby(by='sex')[['Python', 'Java']]  # 单分组
for name, data in g:
    print('组名1：', name)
    print('数据1：', data)
print('-' * 100)
t = df.groupby(by=['class', 'sex'])[['Python']]  # 多分组
for name, data in t:
    print('组名2：', name)
    print('数据2：', data)
print('-' * 100)
# 1.2 对一列值进行分组
df['Python'].groupby(df['class'])  # 单分组
df['Keras'].groupby([df['class'], df['sex']])  # 多分组
# 1.3 按数据类型分组
df.T.groupby(df.dtypes)
# 1.4 通过字典进行分组
m = {'sex': 'category', 'class': 'category', 'Python': 'IT'
    , 'Tensorflow': 'IT', 'Keras': 'IT', 'Java': 'IT', 'C++': 'IT'}
for name, data in df.T.groupby(m):
    print('*' * 100)
    print('组名3', name)
    print('数据3', data)
# 2、分组直接调用函数进行聚合
# 按照性别分组，其他列均值聚合
print('*' * 300)
print(df.groupby(by='sex').mean().round(1))  # 保留1位小数
# 按照班级和性别进行分组，Python、Keras的最大值聚合
print('=' * 300)

print(df.groupby(by=['class', 'sex'])[['Python', 'Keras']].max())
# 按照班级和性别进行分组，计数聚合。统计每个班，男女人数
print('=' * 300)

print(df.groupby(by=['class', 'sex']).size())
# 基本描述性统计聚合
print('=' * 300)

print(df.groupby(by=['class', 'sex']).describe())

# 3、分组后调用apply，transform封装单一函数计算
# 返回分组结果
df.groupby(by=['class', 'sex'])[['Python', 'Keras']].apply(np.mean).round(1)


def normalization(x):
    return (x - x.min()) / (x.max() - x.min())  # 最大值最小值归一化


# 返回全数据，返回DataFrame.shape和原DataFrame.shape一样。
df.groupby(by=['class', 'sex'])[['Python', 'Tensorflow']].transform(normalization).round(3)
