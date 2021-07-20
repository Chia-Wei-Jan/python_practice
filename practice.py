# list 有序、可動
[3, 4, 5]
["Hello", "World"]
# Tuple 有序、不可動
(3, 4, 5)
("Hello", "World")
# Set 集合
{3, 4, 5}
{"Hello", "World"}
# dictionary
{"apple": "蘋果", "data": "資料"}
# calculate
x = 6 / 2.3
x = 7 // 6  # 相當於 C的 /
x = 2 ** 3  # power x = 8

s = "Hello"
s = "Hello\""  # 跳脫 \
s = "Hello" + "world"  # 自串串接
s = "Hello" "world"
s = "QQ" * 2
s = "apple"
s[1:4]  # ppl
s[1:]  # pple
s[:4]  # appl

# -------------------------------------------------------------------------------------------------
# List  有序可變動列表
grades = [12, 60, 15, 70, 90]
grades[0] = 55
grades[1:4] = []  # delete
grades = grades + [17, 58]  # List 串接
length = len(grades)
# print(length)

data = [[3, 4, 5], [6, 7, 8]]
# data[0][1] : 4  , data[1][2] : 8, data[0][0:2] : 3, 4
data[0][0:2] = [5, 5, 5]
# print(data)

# Tuple  有序不可變動列表
data = (3, 4, 5)
# data[0] = 5        error: Tuple 的資料不可更動

# ----------------------------------------------------------------------------------------
# set 集合的運算
s1 = {3, 4, 5}
# print(10 in s1)
# print(10 not in s1)
s2 = {4, 5, 6, 7}
s3 = s1 & s2  # 交集
# print(s3)
s3 = s1 | s2  # 聯集
# print(s3)
s3 = s1 - s2  # 差集: s1中減去s2重疊的部分
# print(s3)
s3 = s1 ^ s2  # 反交集
# print(s3)

s = set("Hello")  # set(string)
# print("H" in s)

# dictionary 字典的運算
dic = {"apple": "蘋果", "bug": "蟲"}
dic["apple"] = "大蘋果"
# print(dic["apple"])
# print("apple" in dic)
# print("test" not in dic)
del dic["apple"]  # 刪除字典中的鍵值對 (key-value pair)
# print(dic)
dic = {x: x * 2 for x in [3, 4, 5]}  # create dictionary from list
# print(dic)

# --------------------------------------------------------------------------------------
'''
x = input("請輸入數字:")   # string
x = int(x)   # change the type to int
if x > 200:
    print("大於200")
elif x>100:
    print("大於100, 小於200")
else:
    print("小於200")
'''

# --------------------------------------------------------------------------------------
''''
num1 = int(input())
num2 = int(input())
op = input("operator: + - * /: ")
if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("Error")
'''

# ---------------------------------------------------------------------------------------
# while 迴圈
'''
n = 1
sum = 0
while n <= 10:
    sum = sum + n
    n += 1
print(sum)
'''

# for迴圈
'''
for x in [3, 5, 6]:
    print(x)
for x in "Hello":
    print(x)
for x in range(5):
    print(x)
for x in range(5,10):
    print(x)
'''

# ----------------------------------------------------------------------------------------------------
# 函式
'''
def multiply(n1, n2):
    return n1 * n2


value = multiply(3, 4) + multiply(5, 6)
print(value)
'''


# --------------------------------------------------------------------------------------------------------
'''
def power(base, exp = 0):
    print(base ** exp)


power(3, 2)
power(4)
power(exp=3, base=2)
'''

# 無限, 不定參數資料

def avg(*ns):
    sum = 0
    for n in ns:
        sum = sum + n
    print(sum/len(ns))


avg(3, 4, 10)

