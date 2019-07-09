#Sock Pair Match
ar = [6,5, 2, 3,5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5]

print(len(ar))
print(max(ar))

count = 0
print(ar)

count = 0
while len(ar) != 0:
    maxim = max(ar)
    ar.remove(max(ar))
    if len(ar) == 0:
        break
    if maxim == max(ar):
        ar.remove(max(ar))
        count += 1
print (count)
