import numpy as np

# 資料形狀
print("-------------------------資料形狀-----------------------------")
data = np.ones(10)
print(data.shape)
data = np.array([
    [3, 1, 4],
    [5, 2, 9],
])
print(data.shape)

# 資料轉置
print("-------------------------資料轉置-----------------------------")
data = np.array([
    [2, 4, 1],
    [5, 3, 1]
])
print('shape: ', data.shape)   # (2,3)
print('T: ', data.T)
print('T.shape: ', data.T.shape)  # (3,2)

# 扁平化資料
print("-------------------------扁平化資料-----------------------------")
data = np.array([
    [
        [1, 2, 3], [4, 5, 6]
    ],
    [
        [7, 8, 9], [10, 11, 12]
    ]
])   # 2x2x3
new_data = data.ravel()
print(new_data)
print(new_data.shape)

# 重塑資料形狀
print("-------------------------重塑資料形狀-----------------------------")
data = np.array([
    [
        [1, 2, 3], [4, 5, 6]
    ],
    [
        [7, 8, 9], [10, 11, 12]
    ]
])   # 2x2x3=12
new_data = data.reshape(3, 4)  # 3x4=12
print(new_data)
new_data = data.reshape(1, 2, 6)
print(new_data)

data = np.zeros(18).reshape(2, 9)
print(data)

data = np.arange(9).reshape(3, 3)
print(data)
print(data.T)