# 作者：顾涛
# 创建时间：2025/7/19
import numpy as np
import matplotlib.pyplot as plt

N = 8
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = np.random.randint(3, 15, size=N)
width = np.pi / 4
colors = np.random.rand(8, 3)  # 随机生成颜色
ax = plt.subplot(111, projection='polar')  # polar表示极坐标
ax.bar(theta, radii, width=width, bottom=0.0, color=colors)
plt.show()
