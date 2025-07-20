# 作者：顾涛
# 创建时间：2025/7/20

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set(style='white', context='paper', font='STKaiti')  # 设置样式
plt.figure(figsize=(9, 6))

x = np.linspace(0, 2 * np.pi, 20)
y = np.sin(x)

# lineplot方法，画一条线
sns.lineplot(x=x, y=y, color='red', ls='--')
sns.lineplot(x=x, y=np.cos(x), color='green', ls='-.')
plt.show()
