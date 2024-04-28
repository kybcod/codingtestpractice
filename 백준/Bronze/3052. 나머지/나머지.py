cnt = 0

n = list(int(input()) for _ in range(10))
answer = []

for num in n:
    a = num % 42
    answer.append(a)
    
    
for i in set(answer):
    cnt += 1
print(cnt)
