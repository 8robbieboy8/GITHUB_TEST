a = [[1,2], [3,4], [5,6]]

print(a)

for i in range(0, 3, 1):
    print(a[i][0])


for i in range(0, len(a), 1):
    print(a[i][0])


b = []
for i in range(0, len(a), 1):
    b. append(a[i][0])

print(b)

b = []
for i in range(0, len(a), 1):
    b.insert(i,a[i][0])

print(b)


