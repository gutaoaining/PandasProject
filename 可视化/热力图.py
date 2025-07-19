# 作者：顾涛
# 创建时间：2025/7/19
import numpy as np
import matplotlib.pyplot as plt

vegetables = ['cucumber', 'tomato', 'lettuce', 'asparagus', 'potato', 'wheat', 'barley']
farmers = list('ABCDEFG')
harvest = np.random.rand(7, 7) * 5  # 数据
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'heavy'
plt.figure(figsize=(8, 8))
im = plt.imshow(harvest)

plt.xticks(np.arange(len(farmers)), farmers, rotation=45, ha='right')
plt.yticks(np.arange(len(vegetables)), vegetables)

# 绘制文本
for i in range(len(vegetables)):
    for j in range(len(farmers)):
        text = plt.text(j, i, round(harvest[i, j], 1),
                        ha='center', va='center', color='r'
                        )
plt.title('Harvest of local farmers', pad=20)
plt.tight_layout()
plt.show()
