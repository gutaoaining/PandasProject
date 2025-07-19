# 作者：顾涛
# 创建时间：2025/7/19
import numpy as np
import matplotlib.pyplot as plt

labels = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6']  # 级别
men_means = np.random.randint(20, 35, size=6)
women_means = np.random.randint(20, 35, size=6)

# men_std = np.random.randint(1, 7, size=6)
# women_std = np.random.randint(1, 7, size=6)
width = 0.35
plt.bar(
    labels,  # 横坐标
    men_means,  # 柱高
    width,  # 线宽
    yerr=4,  # 误差条
    label='Men'  # 标签
)
plt.bar(labels,
        women_means,
        width,
        yerr=2,
        bottom=men_means,
        label='Women'
        )
plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.legend()
plt.show()
