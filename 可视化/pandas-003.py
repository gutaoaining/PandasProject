# 作者：顾涛
# 创建时间：2025/6/29
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def f(x):
    return np.exp(-x) * np.cos(2 * np.pi * x)


x = np.linspace(0, 5, 50)
plt.figure(figsize=(9, 6))
plt.plot(x, f(x), color='purple',
         marker='o',
         ls='--',
         lw=2,
         alpha=0.6,
         markerfacecolor='red',  # 点颜色
         markersize=10,  # 点大小
         markeredgecolor='green',  # 点边缘颜色
         markeredgewidth=3  # 点边缘宽度
         )
plt.xticks(size=18)  # 设置刻度大小
plt.yticks(size=18)
plt.show()
