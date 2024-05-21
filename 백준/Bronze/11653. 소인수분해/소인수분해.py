n = int(input())
i = 2
num_list = []

# 소인수 찾기
while i*i <= n:
    # n이 i로 나누어 떨어지지 않으면 i 증가
    if n % i:
        i += 1
    # 떨어지면 n을 i로 나누고 i 증가하지 않기
    else:
        n //= i
        num_list.append(i)
        
# 루프 종류 후 마지막 소인수
if n > 1:
    num_list.append(n)
    
print("\n".join(map(str, num_list)))
