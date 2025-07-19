# 作者：顾涛
# 创建时间：2025/7/19
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100, 2)
s = np.random.randint(10, 30, size=100)
color = np.random.randn(100)
plt.scatter(data[:, 0],  # 横坐标
            data[:, 1],  # 纵坐标
            s=s,  # 尺寸
            c=color,  # 颜色
            alpha=0.5  # 透明度
            )

plt.show()
