import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

db = json.load(open('datasets/usda_food/database.json'))
# print(db[50])
# 展示json数据字段
# print(db[50].keys())

# 选取需要分析的字段
info_keys = ['description', 'group', 'id', 'manufacturer']
info = pd.DataFrame(db, columns=info_keys)

# 展示nutrients具体内容
df = pd.DataFrame(db[0]['nutrients'])
# print(df)

# 将所有nutrients下属内容纵向合并
nutrients = []
for la in db:
    lbj = pd.DataFrame(la['nutrients'])
    lbj['id'] = la['id']
    nutrients.append(lbj)
nutrients = pd.concat(nutrients,ignore_index=True)

# 计算相同行并进行去重操作
nutrients.duplicated().sum()
nutrients = nutrients.drop_duplicates()

# 为区分相同字段进行字段重命名
col_mapping = {'description' : 'food',
               'group'       : 'fgroup'}
info = info.rename(columns=col_mapping, copy=False)
col_mapping = {'description' : 'nutrient',
               'group' : 'nutgroup'}
nutrients = nutrients.rename(columns=col_mapping, copy=False)

# 将nutrients和info进行数据横向合并
ndata = pd.merge(nutrients,info,how='outer')
# print(ndata)

fig = plt.figure()
result = ndata.groupby(['nutrient', 'fgroup'])['value'].quantile(0.5)
result['Zinc, Zn'].sort_values().plot(kind='barh')
plt.show()
# fig.show()

by_nutrient = ndata.groupby(['nutgroup', 'nutrient'])

get_maximum = lambda x: x.loc[x.value.idxmax()]
get_minimum = lambda x: x.loc[x.value.idxmin()]

max_foods = by_nutrient.apply(get_maximum)[['value', 'food']]

# make the food a little smaller
max_foods.food = max_foods.food.str[:50]
print(max_foods.loc['Amino Acids']['food'])