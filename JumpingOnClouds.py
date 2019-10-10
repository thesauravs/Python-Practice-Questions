c = [0, 0, 1, 0, 0, 1, 0]

hop = 0
print(c)
print(len(c))

for i in range(len(c)):
    if c[i+1] != 0:
        i += 2
        hop += 1
    else:
        if c[i+2] == 0:
            hop += 1
            i += 2
        else:
            hop += 1
            i += 1
print(hop)