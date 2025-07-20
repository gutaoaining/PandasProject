# 作者：顾涛
# 创建时间：2025/7/20
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.figure(figsize=(12, 9))
flights = pd.read_csv('./flights.csv')

flights = flights.pivot(index='month', columns='year', values='passengers')
sns.heatmap(flights, annot=True, fmt='d', cmap='RdBu_r', linewidths=0.5)
plt.show()
