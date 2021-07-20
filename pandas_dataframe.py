import pandas as pd
data = pd.DataFrame({
    "name": ["Amy", "Andy", "David"],
    "math": [60, 70, 80]
}, index=["a", "b", "c"])
print(data)

# 觀察資料
print("-----------------------Observe data------------------------")
print("data size: ", data.size)
print("data shape: ", data.shape)
print("data index: ", data.index)
print("===============================")
# 取得 row 的 Series
print("get second row: ", data.iloc[1], sep="\n")
print("===============================")
print("get c row: ", data.loc["c"], sep="\n")

# 取得 column 的 Series
print("===============================")
print("get name:", data["name"], sep="\n")
names = data["name"]
print("===============================")
print("toupper: ", names.str.upper(), sep='\n')
print("===============================")
maths = data["math"]
print("math mean:", maths.mean())

# 建立新欄位
data["physic"] = [85, 67, 43]
data["English"] = pd.Series([95, 74, 100], index=["a", "b", "c"])
data["AVG"] = (data["math"] + data["physic"] + data["English"]) / 3
print(data)
