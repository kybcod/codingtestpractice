result = 0

total = int(input())
count = int(input())

for i in range(count):
    a,b = map(int, input().split())
    result += (a * b)

if total == result:
    print("Yes")
else:
    print("No")