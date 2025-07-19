# 作者：顾涛
# 创建时间：2025/6/11
import numpy as np
import pandas as pd

df = pd.DataFrame(data=np.random.randint(0, 10, size=(10, 3)), index=list('ABCDEFHIJK'),
                  columns=['Python', 'Java', 'Keras'])

print(f'原始数据：\n{df}')
df.iloc[4, 2] = None
print(f'修改过后的数据：\n{df}')
df.rename(index={'A': 'AA', 'B': 'BB'}, columns={'Python': '人工智能'}, inplace=True)
print(f'重命名列名和行索引过后的数据：\n{df}')
# 替换值
df.replace(3, 1024, inplace=True)
print(f'把3都替换成1024：\n{df}')
df.replace([0, 7], 2048, inplace=True)
print(f'把0和7都替换成2048：\n{df}')
print(f'把0替换成512，把None替换成998:\n{df.replace({1: 512, np.nan: 998})}')
print(f'把Java这一列等于2的替换成-1024：\n{df.replace({'Python': 2}, -1024)}')
