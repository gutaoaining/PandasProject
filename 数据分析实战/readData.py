# 作者：顾涛
# 创建时间：2025/9/1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

job = pd.read_csv('./job.csv')
print(job.shape, job['city'].unique())
columns = ["positionName",
           "companyShortName",
           "city",
           "companySize",
           "education",
           "financeStage",
           "industryField",
           "salary",
           "workYear",
           "companyLabelList",
           "job_detail"]
job = job[columns].drop_duplicates()  # 去重
print(job.shape, job.head())
