n = int(input())
result = 1
cnt = 1
while result < n:
    result += 6*cnt
    cnt += 1
print(cnt)