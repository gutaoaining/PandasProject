# 作者：顾涛
# 创建时间：2025/7/20
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D  # 3D引擎

plt.rcParams['font.family'] = 'Kaiti SC'

month = np.arange(1, 5)
# 每个月 4周 每周都会产生数据
# 三个维度：月、周、销量
fig = plt.figure(figsize=(9, 6))
ax3 = plt.subplot(111, projection='3d')

for m in month:
    # 每个月都要绘制条形图
    ax3.bar(np.arange(1, 5),  # 横坐标
            np.random.randint(1, 10, size=4),  # 纵坐标
            zs=m,
            zdir='x',  # 在哪个方向上，一排排排列
            alpha=0.7,  # alpha透明度
            width=0.5)
ax3.set_xlabel('月份', fontsize=18, color='red')
ax3.set_xticks(month)
ax3.set_ylabel('周', fontsize=18, color='red')
ax3.set_yticks([1, 2, 3, 4])
ax3.set_zlabel('销量', fontsize=18, color='green')
plt.show()
