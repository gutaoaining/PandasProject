# 作者：顾涛
# 创建时间：2025/6/14
import numpy as np
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

df = pd.DataFrame(data=np.random.randint(0, 100, size=(10, 3)), index=list('ABCDEFHIJK'),
                  columns=['Python', 'Java', 'Keras'])
print(f'原始数据：\n{df}')

print(f'转置之后：\n{df.T}')

df2 = pd.DataFrame(data=np.random.randint(0, 100, size=(20, 3)),
                   index=pd.MultiIndex.from_product([list('ABCDEFHIJK'), ['期中', '期末']])  # 多层索引
                   , columns=['Python', 'Java', 'Keras'])
print(f'df2的原始数据：\n{df2}')
# level默认是最内层的index
print(f'行旋转成列，level指定哪一层，进变换：\n{df2.unstack(level=0)}')
print(f'列转成行：\n{df2.stack()}')
print(f'行列互转：\n{df2.stack().unstack(level=1)}')
print(f'各科平均分：\n{df2.mean()}')  # 统计各科平均分
print(f'各科,每个人期中期末的平均分：\n{df2.groupby(level=0).mean()}')  # 统计各科,每个人期末期中平均分
print(f'各科,期中期末平均分：\n{df2.groupby(level=1).mean()}')  # 统计各科,期末期中平均分
