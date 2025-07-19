# 作者：顾涛
# 创建时间：2025/6/14
from pickle import FALSE

import numpy as np
import pandas as pd

df = pd.DataFrame(data=np.random.randint(0, 30, size=(30, 3)), index=list('qwertyuioijhgfcasdcvbnerfghjcf'),
                  columns=['Python', 'Keras', 'Pytorch'])
print(f'原始数据：\n{df}')
# 1、索引列表名称
print(f'按升序排序之后：\n{df.sort_index(axis=0, ascending=True)}')  # 按索引排序
print(f'按降序排序之后：\n{df.sort_index(axis=0, ascending=False)}')  # 按索引排序
# 2、属性值排序
print(df.sort_values(by=['Python']))  # 按Python属性值排序
print(df.sort_values(by=['Python', 'Keras']))  # 先按Python，再按Keras排序
# 3、返回属性n大或者n小的值
print(df.nlargest(10, columns='Keras'))  # 根据属性Keras排序，返回最大10个数据
print(df.nsmallest(2, columns='Python'))  # 根据属性Python排序，返回最小2个数据
