# 作者：顾涛
# 创建时间：2025/6/29

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 50)
y = np.sin(x)

# 子视图1
plt.figure(figsize=(9, 6))
ax = plt.subplot(221)  # 两行两列第一个子视图
ax.plot(x, y, color='red')
ax.set_facecolor('green')  # 调用子视图设置方法，设置子视图整体属性

# 子视图2
ax = plt.subplot(2, 2, 2)  # 两行两列第二个子视图
line, = ax.plot(x, -y)  # 返回绘制对象
line.set_marker('*')  # 调用对象设置方法，设置属性
line.set_markerfacecolor('red')
line.set_markeredgecolor('green')
line.set_markersize(10)

# 子视图3
ax = plt.subplot(2, 1, 2)  # 两行一列第二行试图
plt.sca(ax)  # 设置当前视图
x = np.linspace(-np.pi, np.pi, 200)
plt.plot(x, np.sin(x * x), color='red')
plt.show()
