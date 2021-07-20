import pandas as pd
# 建立 Series
print("---------------------Series-----------------------")
data = pd.Series([5, 10, 15])
print(data)
print("Max: ", data.max())
print("Median: ", data.median())

data = data * 2
print(data)

data = data == 10
print(data)

# 建立 DataFrame
print("-------------------DataFrame-----------------------")
data = pd.DataFrame({
    "name": ["Amy", "Andy", "David"],
    "score": [60, 70, 80]
})
print(data)
print("=====================================")
print(data["name"])
print("=====================================")
print(data["score"])
print("=====================================")
print(data.iloc[0])
