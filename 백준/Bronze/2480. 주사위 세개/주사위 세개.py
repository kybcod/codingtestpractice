a, b, c = map(int, input().split())
reward = 0

if a == b == c:  # 모두 같은 경우
    reward = 10000 + a * 1000
elif a == b or a == c or b == c:  # 두 개의 눈이 같은 경우
    if a == b == c:
        reward = 10000 + a * 1000
    else:
        if a == b:
            reward = 1000 + a * 100
        elif a == c:
            reward = 1000 + a * 100
        elif b == c:
            reward = 1000 + b * 100
else:  # 모두 다른 경우
    reward = max(a, b, c) * 100

print(reward)
