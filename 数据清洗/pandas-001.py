# 作者：顾涛
# 创建时间：2025/6/8

import numpy as np
import pandas as pd

df = pd.DataFrame(
    data={'color': ['red', 'blue', 'red', 'green', 'blue', None, 'red', np.nan],
          'price': [10, 20, 10, 13, 20, 0, np.nan, None]})  # 对于数字而言，np.nan和None显示都是NaN
# 1、重复数据过滤
print(f'原始数据：\n{df}')
# 判断是否存在重复数据
print()
print(df.duplicated())
# 删除重复数据
print()
print(df.drop_duplicates())

print()
# 计算时，None和NaN没有区别
# None Python的数据类型
# NaN是Numpy的数据类型
# 都表示空数据
print(df.fillna(1024))
print()
# 指定行或者列过滤
# del df['color']  # 直接删除某列
# print()
# print(f'删除color列数据：\n{df}')
# ！！！drop删除、返回值，原来的数据就没有改变
# 没有修改原数据
df.drop(labels=['price'], axis=1)  # 删除指定列
print(df.drop(labels=['price'], axis=1))
print()
print(f'删除price列原数据：\n{df}')

print()
df.drop(labels=[0, 1, 5], axis=0)  # 删除指定行
print(df.drop(labels=[0, 1, 5], axis=0))  # 删除指定行)
print()
print(f'删除指定行的原数据数据：\n{df}')

print()
print(f'原始数据：\n{df}')

# 修改原数据,inplace表示修改的值是否替代原值
print()
print(df.drop(labels=[0, 1, 3, 5], axis=0, inplace=True))  # 删除指定行)
print(f'原始数据：\n{df}')
