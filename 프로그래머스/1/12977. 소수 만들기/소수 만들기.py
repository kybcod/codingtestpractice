from itertools import combinations

def solution(nums):
    answer = []
    combi = list(combinations(nums, 3))
    
    for com in combi:
        num = sum(com)
        
        is_prime = True
        # 합이 소수인지 확인
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                
        if is_prime:
            answer.append(num)

    return len(answer)