# 作者：顾涛
# 创建时间：2025/6/15
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1、线形图
# df1 = pd.DataFrame(data=np.random.randn(1000, 4),
#                    index=pd.date_range(start='27/6/2021', periods=1000), columns=list('ABCD'))
# plt.plot(df1.cumsum())
# plt.show()  # 保存图片
# 2、条形图
# df2 = pd.DataFrame(data=np.random.randn(10, 4),
#                    columns=list('ABCD'))
# print(f'\n{df2}')
# df2.plot.bar(stacked=False)  # stacked是否堆叠
# plt.show()  # 保存图片

# 3、饼图
# df3 = pd.DataFrame(data=np.random.rand(4, 2),
#                    index=list('ABCD'),
#                    columns=['One', 'Two'])
# df3.plot.pie(subplots=True, figsize=(8, 8), colors=np.random.random(size=(4, 3)))
# plt.show()

# 4、散点图,描述两者之间的关系
# df4 = pd.DataFrame(np.random.randint(0, 50, size=(50, 4)), columns=list('ABCD'))
# df4['F'] = df4['C'].map(lambda x: x + np.random.randint(-5, 5, size=1)[0])
# df4.plot.scatter(x='C', y='F')  # C和F关系绘制
# plt.show()

# 5、面积图
df5 = pd.DataFrame(data=np.random.rand(10, 4),
                   columns=list('ABCD'))
df5.plot.area(stacked=True, color=np.random.rand(4, 3))  # stacked 是否堆叠
plt.show()
