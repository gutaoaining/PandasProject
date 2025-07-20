# 作者：顾涛
# 创建时间：2025/7/20
import matplotlib.pyplot as plt

plt.figure(figsize=(9, 6))
days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]
plt.stackplot(days, sleeping, eating, working, playing)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Stack plot', fontsize=18)
plt.legend(['Sleeping', 'Eating', 'Working', 'Playing'], fontsize=18)
plt.show()
