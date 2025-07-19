# 作者：顾涛
# 创建时间：2025/6/14
import numpy as np
import pandas as pd

df = pd.DataFrame(data=np.random.randint(0, 100, size=(20, 3)), index=list('ABCDEFHIJKLMNOPQRSTU'),
                  columns=['Python', 'Java', 'Keras'])
print(f'原始数据:\b{df}')
# 1、简单统计指标
print(df.count())  # 非NA值的数量
print(df.max(axis=0))  # 轴0最大值，即每一列最大值
print(df.min())  # 默认计算轴0最小值
print(df.median())  # 中位数
print(df.sum())  # 求和
print(df.mean(axis=1))  # 每行平均值
print(df.quantile(q=[0.2, 0.4, 0.8]))  # 分位数
print(df.describe())  # 查看数值型列的汇总金额，计数，平均数，标准差，最小值

# 索引位置
print(df['Python'].argmin())  # 计算最小值位置
print(df['Python'].argmax())  # 计算最大值位置
print(df.idxmax())  # 最大值索引标签
print(df.idxmin())  # 最小值索引标签

# 更多指标统计
print(df['Python'].value_counts())  # 统计元素出现次数
print(df['Keras'].unique())  # 去重
print(df.cumsum())  # 累加
print(df.cumprod())  # 累乘
print(df.std())  # 标准差
print(df.var())  # 方差
print(df.cummin())  # 累计最小值
print(df.cummax())  # 累计最大值
print(df.diff())  # 计算差分
print(df.pct_change())  # 计算百分比变化

# 高级统计指标
print(df.cov())  # 属性协方差
print(df['Python'].cov(df['Keras']))  # Python和Keras的协方差
print(df.corr())  # 所有属性相关性系数
print('-' * 100)
print(df.corrwith(df['Java']))  # 单一属性相关性系数
