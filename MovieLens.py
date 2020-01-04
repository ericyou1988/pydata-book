import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('datasets/movielens/users.dat', sep='::',
                      header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('datasets/movielens/ratings.dat', sep='::',
                        header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('datasets/movielens/movies.dat', sep='::',
                       header=None, names=mnames)
data = pd.merge(pd.merge(ratings, users), movies)
# 按性别计算每部电影平均分
mean_ratings = data.pivot_table('rating', index='title',
                                columns='gender', aggfunc='mean')
print(mean_ratings)
# 选出评论数大于250的作为活跃样本
ratings_by_title = data.groupby('title').size()
active_titles = ratings_by_title.index[ratings_by_title >= 250]
mean_ratings = mean_ratings.loc[active_titles]
# 计算女性观众最喜欢的电影
top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
print(top_female_ratings[:10])
# 选出分歧最大且女性更喜欢的电影
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_values(by='diff')
print(sorted_by_diff[:10])
# 对排序结果反序则为男生更喜欢
print(sorted_by_diff[::-1][:10])
# 找出分歧最⼤的电影（不考虑性别因素）计算得分数据的⽅差
rating_std_by_title = data.groupby('title')['rating'].std()
rating_std_by_title = rating_std_by_title.loc[active_titles]
print(rating_std_by_title.sort_values(ascending=False)[:10])
