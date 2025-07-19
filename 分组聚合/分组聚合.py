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
# agg多种统计汇总操作
# 分组后调用agg应用多种统计汇总
print(df.groupby(by=['class', 'sex'])[['Tensorflow', 'Keras']].agg([np.max, np.min, pd.Series.count]))
# 分组后不同属性应用多种不同统计汇总
print(df.groupby(by=['class', 'sex'])[['Python', 'Keras']].agg(
    {'Python': [('最大值', np.max), ('最小值', np.min)], 'Keras': [('计数', pd.Series.count), ('中位数', np.median)]}))



