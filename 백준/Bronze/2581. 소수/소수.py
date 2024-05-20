import math

def is_Prime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

prime_list = []
m = int(input())
n = int(input())
for i in range(m, n+1):
    if is_Prime(i) == True:
        prime_list.append(i)
if len(prime_list) == 0:
        print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))

