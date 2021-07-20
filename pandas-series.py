import pandas as pd
# 資料索引
data = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
print(data)

# 觀察資料
print("--------------------Observe data---------------------------")
print("data type: ", data.dtype)
print("data size: ", data.size)
print("data index: ", data.index)

# 取得資料: 根據順序、根據索引
print("----------------------Get data------------------------------")
print(data[2], data[1])
print(data["e"], data["c"])

# 數字運算: 基本、統計、順序
print("-------------------Numerical operations----------------------")
print("max: ", data.max())
print("sum: ", data.sum())
print("standard deviation: ", data.std())
print("median: ", data.median())
print("largest: ", data.nlargest(2))


# 字串運算: 基本、串接、搜尋、取代
print("-------------------String operations--------------------------")
data = pd.Series(["ANDY", "DAVID", "PETER"])
print(data.str.lower())
print(data.str.len())
print(data.str.cat(sep=" "))
print(data.str.contains("D"))
print(data.str.replace("ANDY", "TOM"))
