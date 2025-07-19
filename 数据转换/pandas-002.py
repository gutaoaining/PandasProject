# 作者：顾涛
# 创建时间：2025/6/12
import numpy as np
import pandas as pd

df = pd.DataFrame(data=np.random.randint(0, 10, size=(10, 3)), index=list('ABCDEFHIJK'),
                  columns=['Python', 'Java', 'Keras'])

print(f'原始数据：\n{df}')
df.iloc[4, 2] = None
print(f'修改过后的数据：\n{df}')

print(f'map修改过后的数据：\n{df['Keras'].map({1: 'Hello', 5: 'world', 7: 'AI'})}')


def convert(x):
    print(x)
    if x == 1:
        return 'Hello'
    elif np.isnan(x):
        return 'test'
    elif x == 5:
        return 'world'
    else:
        return 'AI'


print(f'自定义函数修改：\n{df['Keras'].map(convert)}')
print(df['Python'].map(lambda x: True if x >= 5 else False))  # 隐式函数映射
df['Java'].map(lambda x: True if x > 5 else False)
