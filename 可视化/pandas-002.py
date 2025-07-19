# 作者：顾涛
# 创建时间：2025/6/29

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 20)
y1 = np.sin(x)
y2 = np.cos(x)

# 设置颜色，线型，点型
plt.plot(x, y1, color='indigo', ls='-.', marker='p')
plt.plot(x, y2, color='#FF00EE', ls='--', marker='o')
plt.plot(x, y1 + y2, color=(0.2, 0.7, 0.2), ls=':', marker='*')
plt.plot(x, y1 + 2 * y2, linewidth=3, alpha=0.7, color='orange')  # 线型，透明度
plt.plot(x, 2 * y1 + y2, 'bo--')  # 参数连用
plt.show()
