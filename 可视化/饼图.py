# 作者：顾涛
# 创建时间：2025/7/19
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# 解决中文字体乱码的问题
matplotlib.rcParams['font.sans-serif'] = 'Kaiti SC'
labels = ['五星', '四星', '三星', '二星', '一星']  # 标签
percent = [95, 261, 105, 30, 9]  # 某市星级的酒店数量
# 设置图片大小和分辨率
fig = plt.figure(figsize=(5, 5), dpi=150)
# 偏移中心量，凸出来某一部分
explode = (0, 0.1, 0, 0, 0)
# 绘制饼图，autopct显示百分比，这里保留一位小数，shadow控制是否显示阴影
plt.pie(x=percent,  # 数据
        explode=explode,  # 偏移中心量
        labels=labels,  # 显示标签
        autopct='%0.1f%%',  # 显示百分比
        shadow=True  # 阴影，3D效果
        )
plt.show()