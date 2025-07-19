import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 100)
data1 = np.exp(x)
data2 = np.sin(x)
plt.figure(figsize=(9, 6))
plt.rcParams['font.size'] = 16  # 设置整体字体大小
ax1 = plt.gca()  # 获取当前轴域
ax1.set_xlabel('time (s)')  # 设置x轴标签
ax1.set_ylabel('exp' , color='red')  # 设置y轴标签
ax1.plot(x, data1, color='red')  # 数据绘制
ax1.tick_params(axis='y', labelcolor='red')  # 设置y轴刻度属性
ax2 = ax1.twinx()  # 创建新axes实例，共享x轴，并设置
ax2.set_ylabel('sin', color='blue')
ax2.plot(x, data2, color='blue')
ax2.tick_params(axis='y', labelcolor='blue')
plt.tight_layout()  # 紧凑布局
plt.show()
