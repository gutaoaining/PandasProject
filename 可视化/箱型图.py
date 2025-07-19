# 作者：顾涛
# 创建时间：2025/7/19
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(size=(500, 4))
labels = ['A', 'B', 'C', 'D']
# 用matplotlib画箱线图
# 查看数据分布情况，看异常值
plt.boxplot(data, 1, 'ro', labels=labels)  # 红色的原点是异常值
plt.show()
