# Instance Attributes

# Point 實體物件的設計: 平面座標上的點
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(1, 2)
print(p1.x, p1.y)
p2 = Point(3, 4)
print(p2.x, p2.y)
"""

# -------------------------------------------------------------------------------------------
# 成績單
"""
class list:
    def __init__(self, name, score):
        self.name = name
        self.score = score


student1 = list("David", 50)
student2 = list("Amy", 80)
print(student1.name, student1.score)
print(student2.name, student2.score)
"""

# ----------------------------------------------------------------------------------------------------
# Instance Methods

# Point 實體物件的設計； 平面座標上的點
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 定義實體方法
    def show(self):
        print(self.x, self.y)

    def distance(self, targetX, targetY):
        return (((self.x - targetX) ** 2) + ((self.y - targetY) ** 2)) ** 0.5


p = Point(3, 4)
p.show()   # 呼叫實體方法 / 函式
result = p.distance(0, 0)   # (3,4) 和 (0,0) 的距離
print(result)
"""


# ----------------------------------------------------------------------------------------------------------
# File 實體物件的設計: 包裝檔案讀取的函式
class File:
    def __init__(self, name):
        self.name = name
        self.file = None  # None

    def open(self):
        self.file = open(self.name, mode="r", encoding="utf-8")

    def read(self):
        return self.file.read()


f1 = File("data1.txt")
f1.open()
data = f1.read()
print(data)

