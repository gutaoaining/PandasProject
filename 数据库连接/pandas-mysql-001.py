# 作者：顾涛
# 创建时间：2025/6/8
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

df = pd.DataFrame(data=np.random.randint(0, 50, size=(150, 3)), columns=['python', 'java', 'keras'])
# 创建数据库连接
conn = create_engine('mysql+pymysql://root:Gutao1111@localhost/mytest?charset=UTF8MB3')
# 保存到数据库
df.to_sql('score', conn, if_exists='append')
# 从数据库中加载
print(pd.read_sql('select * from score limit 10;', conn, index_col='python'))
