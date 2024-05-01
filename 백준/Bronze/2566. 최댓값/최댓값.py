alist = []
for _ in range(9):
    a = list(map(int, input().split()))
    alist.append(a)

max_list = list(map(max, alist))
max_value = max(max_list)
print(max_value)

for i,row in enumerate(alist):
    if max_value in row:
        print(i+1, row.index(max_value)+1)