import pandas as pd

# Series 篩選
print("--------------------Series 篩選----------------------")
data = pd.Series([10, 15, 20])
condition = data > 14
print(condition)
filter = data[condition]
print(filter)
print("=========================")

data = pd.Series(["David", "Peter", "Tom"])
condition = [True, False, True]
filter = data[condition]
print(filter)
print("=========================")

condition = data.str.contains("T")
print(data[condition])


# DataFrame 篩選
print("--------------------DataFrame 篩選------------------------")
data = pd.DataFrame({
    "name": ["Amy", "Andy", "David"],
    "Math": [60, 70, 80],
    "English": [90, 75, 80]
}, index=["a", "b", "c"])
print(data)
print("=========================")

condition = [False, True, True]
print(data[condition])
print("=========================")

condition = data["English"] >= 80
print(condition)
print()
print(data[condition])
print("=========================")

condition = data["name"] == "Amy"
print(condition)
print()
print(data[condition])


