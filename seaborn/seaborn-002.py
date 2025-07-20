# 作者：顾涛
# 创建时间：2025/7/20

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set(style='dark', context='notebook', font='Kaiti SC')  # 设置样式
plt.figure(figsize=(9, 6))
fmri = pd.read_csv('./fmri.csv')  # 核磁共振测试数据
# lineplot()函数作用是绘制线型图。参数x、y，表示横纵坐标；参数hue，表示根据属性分类绘制两条线
# （"event"属性分两类"stim"、"cue"）；参数style，表示根据属性分类设置样式，实线和虚线；参数
# data，表示数据；参数marker、markersize，分别表示画图标记点以及尺寸大小！
ax = sns.lineplot(x='timepoint', y='signal',
                  hue='event', style='event',
                  data=fmri,
                  palette='deep',
                  markers=True,
                  markersize=10
                  )
plt.xlabel('时间节点', fontsize=30)
plt.show()
