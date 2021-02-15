from pandas import Series, DataFrame
import pandas as pd
import numpy as np
#打开文件
car_complain=pd.read_csv('car_complain.csv')
#拆分problem并建表
df=car_complain.drop('problem',axis=1).join(car_complain.problem.str.get_dummies(','))
#获取问题标签
tags=df.columns[7:]
#品牌总投诉量
df['brand']=df['brand'].replace('一汽-大众','一汽大众')
result=df.groupby(['brand'])['id'].agg(['count'])
result_by_brand=df.groupby(['brand'])[tags].agg(['sum'])
#合并表格
result=result.merge(result_by_brand,left_index=True,right_index=True,how='left')
result.reset_index(inplace=True)
#品牌投诉总数排名
result_order=result.sort_values('count', ascending=False) #吉利投诉最多96
print(result_order)

#车型投诉排名
result_by_car_model=df.groupby(['car_model'])['id'].agg(['count'])
result_by_car_model=result_by_car_model.sort_values('count',ascending=False) #阿特兹75个投诉
print(result_by_car_model)

#品牌的平均车型投诉排名
result2=car_complain.groupby(['brand'])['car_model'].agg(['nunique'])
result3=car_complain.groupby(['brand'])['car_model'].agg(['count'])
result_mean=result3['count']/result2['nunique']
print(result_mean.sort_values(ascending=False)) #一汽马自达47.5

