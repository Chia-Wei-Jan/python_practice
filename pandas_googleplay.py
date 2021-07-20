import pandas as pd
import re
# 讀取資料
data = pd.read_csv("googleplaystore.csv")    # read csv file as DataFrame
# 觀察資料
print("----------------------Observe Data------------------------")
print(data)
print("data quantity: ", data.shape)
print("data column: ", data.columns, sep='\n')

# 分析資料: 評分的各種統計數
print("---------------------Analyze Data: Rating--------------------")
condition = data["Rating"] <= 5
data = data[condition]
print("Average: ", data["Rating"].mean())
print("Median: ", data["Rating"].median())
print("Average of top 500 apps: ", data["Rating"].nlargest(500).mean())

# 分析資料: 安裝數量的各種統計數據
print("-------------------Analyze Data: Installs--------------------")
data["Installs"] = data["Installs"].str.replace(",", "")
data["Installs"] = data["Installs"].str.replace("+", "")
data["Installs"] = data["Installs"].str.replace("Free", "")
data["Installs"] = pd.to_numeric(data["Installs"])
print("Average of installs: ", data["Installs"].mean())
condition = data["Installs"] > 100000
print("Apps more than 100000 installs: ", data[condition].shape[0])

# 基於資料的應用: 關鍵字搜尋應用程式名稱
print("---------------------Search Keyword--------------------------")
keyword = input("Please input keyword: ")
condition = data["App"].str.contains(keyword, case=False)
print(data[condition]["App"])
print("Number of apps containing keyword: ", data[condition].shape[0])
