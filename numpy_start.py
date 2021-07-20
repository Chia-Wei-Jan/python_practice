import numpy as np
ndarr = np.array([3, 4, 5])    # 根據列表建立 ndarray 物件
print(ndarr)
print(ndarr.size)

# 建立一維陣列
print('--------------------一維陣列---------------------------')
data = np.array([3, 2, 6, 4])
print('np.array([3, 2, 6, 4]):\t', data)
data = np.empty(2)
print('np.empty(2):\t', data)
data = np.zeros(3)
print('np.zeros(3):\t', data)
data = np.ones(3)
print('np.ones(3):\t', data)
data = np.arange(5)
print('np.arange(5):\t', data)

# 建立二維陣列
print('--------------------二維陣列---------------------------')
data = np.array([    # 3x3 array
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])
print(data)
data = np.empty([3, 3])
print(data)
data = np.zeros([1, 2])
print(data)
data = np.ones([2, 3])
print(data)

# 建立三維陣列
print('--------------------三維陣列---------------------------')
data = np.array([   # 2x2x2 array
    [
        [1, 2], [3, 4]
    ],
    [
        [5, 6], [7, 8]
    ],
])
print(data)
data = np.zeros([3, 1, 3])    # 3x1x3 array
print(data)

# 建立高維陣列
print('--------------------高維陣列---------------------------')
data = np.array([   # 1x1x2x3
    [
        [
            [3, 2, 1],
            [5, 5, 10]
        ]
    ]
])
print(data)
data = np.ones([2, 1, 1, 2])
print(data)

# 逐元運算 (elementwise)
print('--------------------逐元運算---------------------------')
data1 = np.array([3, 2, 10])
data2 = np.array([1, 3, 6])
print('data1:\t', data1)
print('data2:\t', data2)
result = data1 + data2
print('加法:\t', result)
result = data1 * data2
print('乘法:\t', result)
result = data1 > data2
print("大於:\t", result)
result = data1 == data2
print("相等:\t", result)

# 矩陣運算 (matrix)
data1 = np.array([
    [1, 2]
])   # 1x2
data2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])   # 2x3
# result = data1.dot(data2)    # 1x3
# print(result)
result = data1 @ data2
print('內積:\t', result)
result = np.outer(data1, data2)   # 2x6
print('外積:\t', result)

# 統計運算 (statistics)
data = np.array([
    [2, 1, 7],
    [-5, 3, 8]
])   # 2x3
result = data.sum()
print("總和: ", result)
result = data.max()
print("max: ", result)
result = data.min()
print("min: ", result)
result = data.mean()
print("average: ", result)
result = data.std()
print("標準差: ", result)

result = data.sum(axis=0)  # sum of column
print('sum of column: ', result)
result = data.sum(axis=1)  # sum of row
print('sum of row: ', result)
result = data.max(axis=0)
print(result)
result = data.mean(axis=1)
print(result)

result = data.cumsum()
print('cumsum(): ', result)
result = data.cumsum(axis=0)
print('cumsum(axis=0): ', result)

