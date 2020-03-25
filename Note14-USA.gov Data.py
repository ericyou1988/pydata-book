import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

path = 'datasets/bitly_usagov/example.txt'
records = [json.loads(line) for line in open(path)]
# print(records[0])

# 生成DataFrame数据
frame = pd.DataFrame(records)
print(frame.info(),frame['tz'][:10])
# 统计tz字段最大的10位
tz_counts = frame['tz'].value_counts()
print(tz_counts[:10])
# fillna函数替换缺失值（NA） 未知值（空字符串）通过布尔型数组索引替换
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])
# 用水平柱状图展示前10位出现
fig = plt.figure(figsize=(10, 4))
subset = tz_counts[:10]
sns.barplot(y=subset.index, x=subset.values)
plt.show()
# 提取浏览器信息
results = pd.Series([x.split()[0] for x in frame.a.dropna()])
print(results[:5])
print(results.value_counts()[:8])
# 舍弃确实字段a的数据
cframe = frame[frame.a.notnull()]
cframe = cframe.copy()
# 计算是否含有windows字符串
cframe['os'] = np.where(cframe['a'].str.contains('Windows'),
                        'Windows', 'Not Windows')
print(cframe['os'][:5])
# 对时区和操作系统进行聚类分析
by_tz_os = cframe.groupby(['tz', 'os'])
agg_counts = by_tz_os.size().unstack().fillna(0)
print(agg_counts[:10])
# # 不同的方法显示
# by_tz_os2 = cframe.pivot_table('nk',index='tz',columns='os',aggfunc='count',fill_value=0)
# by_tz_os2[:10]
# 取行相加数值最大的10组数据
count_win = agg_counts.sum(1).nlargest(10)
k1 = agg_counts.reindex(count_win.index)
k1.plot(kind='barh')
plt.show()
#  按每一组的比例作图
k2 = k1.div(k1.sum(1),axis=0)
k2.plot(kind='barh')
plt.show()


