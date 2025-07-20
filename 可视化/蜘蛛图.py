# 作者：顾涛
# 创建时间：2025/7/20
import numpy as np
import matplotlib.pyplot as plt
from sympy.printing.pretty.pretty_symbology import line_width

plt.rcParams['font.family'] = 'Kaiti SC'
labels = np.array(["个人能力", "IQ", "服务意识", "团队精神", "解决问题能力", "持续学习"])
y = [83, 61, 95, 67, 76, 88]
# 画图数据准备，角度，状态值
x = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
y = np.concatenate([y, [y[0]]])  # 首尾相连
x = np.concatenate([x, [x[0]]])
# 用Matplotlib画蜘蛛图
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, polar=True)
ax.plot(x, y, 'r*--', linewidth=2)  # 连线
ax.fill(x, y, alpha=0.25)  # 填充
# 设置角度
# 这里设置成-1是因为原本数组就是6个，新增一个之后是7个，所以要排除一个
ax.set_thetagrids(x[:-1] * 180 / np.pi,  # 角度值
                  labels,
                  fontsize=18
                  )
# ax.set_rgrids([20, 40, 60, 80], fontsize=18)
plt.show()
