import numpy as np
# 合併陣列
print("------------------------stacking--------------------------")
arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])  # 2x3
arr2 = np.array([
    [7, 8, 9],
    [10, 11, 12]
])  # 2x3

arr3 = np.array([
    [13, 14],
    [15, 16]
])  # 2x2

result1 = np.vstack((arr1, arr2))  # vertical
print(result1)
result2 = np.hstack((arr1, arr2, arr3))  # horizontal
print(result2)

# 分割陣列
print("------------------------splitting-------------------------------")
arr = np.array([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12]
])  # 2x6

result = np.vsplit(arr, 2)  # vertical
# 1x6
# 1x6
print(result)

result = np.hsplit(arr, 2)  # horizontal
# 2x3
# 2x3
print(result)
