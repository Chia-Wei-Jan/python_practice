'''
file = open("data.txt", mode="w", encoding="utf-8")
file.write("測試")
file.close()
'''

# ------------------------------------------------------------------------------

with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("5\n4\n3")


sum = 0
with open("data.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        sum += int(line)
print(sum)

