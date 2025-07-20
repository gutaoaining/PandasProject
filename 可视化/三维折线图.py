# 作者：顾涛
# 创建时间：2025/7/20
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D  # 3D引擎

x = np.linspace(0, 60, 300)
y = np.sin(x)
z = np.cos(x)

fig = plt.figure(figsize=(9, 6))  # 二维图形
ax3 = plt.subplot(111, projection='3d')
ax3.plot(x, y, z)  # 三维折线图
ax3.set_xlabel("X")
ax3.set_ylabel("Y")
ax3.set_zlabel("Z")

# 3维散点图
x = np.random.randint(0, 60, size=20)
y = np.random.randn(20)
z = np.random.randn(20)
ax3.scatter(x, y, z, color='red', s=100)
# 调试试图的角度
ax3.view_init(elev=20, azim=-30)
plt.show()
