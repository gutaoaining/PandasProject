# 作者：顾涛
# 创建时间：2025/7/19
import numpy as np
import matplotlib.pyplot as plt

mu = 100  # 平均值
sigma = 15  # 标准差
x = np.random.normal(loc=100, scale=15, size=10000)
fig, ax = plt.subplots()

n, bins, patches = ax.hist(x, 200, density=True)  # 直方图
# 概率密度函数
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))
plt.plot(bins, y, '--')
plt.xlabel('Smarts')
plt.ylabel('Probability density')
plt.title(r'Histogram of IQ: $\mu=100$,$\sigma=15$')

# 紧凑布局
fig.tight_layout()
plt.show()
