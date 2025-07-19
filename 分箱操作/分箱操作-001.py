# 作者：顾涛
# 创建时间：2025/6/15
import numpy as np
import pandas as pd

df = pd.DataFrame(data=np.random.randint(0, 150, size=(100, 3)),
                  columns=['Python', 'Tensorflow', 'Keras'])
print(f'原始数据：\n{df}')
# 1、等宽分箱
print(f'等宽分箱：\n{pd.cut(df.Python, bins=3)}')
# 指定宽度分箱
print(pd.cut(df.Keras,  # 分箱数据
             bins=[0, 60, 90, 120, 130],  # 分箱断点
             right=False,  # 左闭右开
             labels=['不及格', '中等', '良好', '优秀']  # 分箱后分类
             ))
# 等频分箱
print(pd.qcut(df.Python, q=4,  # 4等分
              labels=['差', '中', '良', '优']  # 分箱后分类
              ))
