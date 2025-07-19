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


# 5、透视表
# 透视表也是一种分组聚合运算
def count(x):
    return len(x)


print(df.pivot_table(values=['Python', 'Keras', 'Tensorflow'],  # 要透视分组的值
                     index=['class', 'sex'],  # 分组透视指标
                     aggfunc={'Python': [('最大值', 'max')],  # 聚合运算
                              'Keras': [('最小值', 'min'), ('中位数', 'median')],
                              'Tensorflow': [('最小值', 'min'), ('平均值', 'mean'), ('计数', count)]
                              }))
