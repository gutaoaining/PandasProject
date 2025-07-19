# 作者：顾涛
# 创建时间：2025/6/8
from operator import index

import numpy as np
import pandas as pd

df = pd.DataFrame(np.array(([3, 7, 1], [2, 8, 256])), index=['dog', 'cat'], columns=['China', 'America', 'France'])
print(df)
print()
print(f'过滤出China和France：\n{df.filter(items=['China', 'France'])}')
# 更具正则表示式选择列标签
print(f'选择a结尾的列名的数据:\n{df.filter(regex='a$', axis=1)}')
# 选择行中包含og的
print(f'选择行中包含og的数据:\n{df.filter(regex='og', axis=0)}')

# 5.异常值过滤
df2 = pd.DataFrame(data=np.random.randn(10000, 3))  # 正太分布的数据
# 3σ过滤异常值，σ即是标准差
cond = df2.abs() > 3 * df2.std()
cond_ = cond.any(axis=1)
print(f'过滤出来的异常值：\n{df2[cond_]}')

cond_0 = cond[0]  # 默认[]。只能取列索引
cond_1 = cond[1]
cond_2 = cond[2]
cond__ = cond_0 | cond_1 | cond_2
print(f'过滤出来的异常值：\n{df2[cond__]}')
