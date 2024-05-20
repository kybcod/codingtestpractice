n,k = map(int, input().split())
n_list = []

for j in range(1,n+1):
    if (n % j == 0):
        n_list.append(j)
if len(n_list) < k:
    print("0")
else:
    print(n_list[k-1])    