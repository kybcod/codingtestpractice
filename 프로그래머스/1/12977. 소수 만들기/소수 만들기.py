import math
from itertools import combinations

def solution(nums):
    result = []
    com = list(combinations(nums,3))
    for i in com:
        num = sum(i)
        print(num)

        #모든 정수 반복(2~n-1까지)
        # for num in range(2,n+1): 
        is_prime = True

        # num = 2,3일 때는 range(2, 2)가 되므로 반복문 실행X 
        # is_prime = True 유지
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                is_prime = False #소수 아님
                break
        if is_prime: #소수가 참이면
            result.append(num) #리스트에 저장

    return len(result)