import random

x,y,z = 3, 3, 3

a = []
for i in range(x):
    temp = []
    for j in range(y):
        temp.append([random.randint(0, 5)])
    a.append(temp)
print(a)