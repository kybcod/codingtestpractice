import math

def is_Prime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n = int(input())
prime_list = []
count = 0
numbers = list(map(int, input().split()))

for num in numbers:
    if is_Prime(num) == True:
        count += 1
        
print(count)