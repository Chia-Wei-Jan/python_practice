# random module
import random
# 隨機選取  choice / sample
# data = random.choice([1, 5, 6, 10, 20])
# data = random.sample([1, 5, 6, 10, 20], 3)
# print(data)

# 隨機調換順序  shuffle
# data = [1, 5, 8, 20]
# random.shuffle(data)
# print(data)

# 隨機取得亂數
# data = random.random()   # random value from 0 to 1
# data = random.uniform(60, 100)     # random value from 60 to 100
# print(data)

# 取得常態分配亂數
# 平均數 100, 標準差 10, 得到的資料多數在 90-110
# data = random.normalvariate(100, 10)
# print(data)

# -------------------------------------------------------------------------------------------------
# statistics module
import statistics as stat
# data = stat.mean([1, 4, 5, 8])
# data = stat.median([1, 4, 5, 8])
data = stat.stdev(([1, 4, 5, 8]))
print(data)
