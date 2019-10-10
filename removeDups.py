list = [1, 2, 3, 1, 1, 1, 4, 5, 6, 4, 1]
newList = []

for num in list:
    if(num not in newList):
        newList.append(num)

print(newList)
