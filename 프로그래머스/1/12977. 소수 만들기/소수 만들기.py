from itertools import combinations

#소수 찾기
def is_Prime(n):
    for j in range(2,n):
        if n % j == 0:
            return False
    return True


def solution(nums):
    sums = [sum(i) for i in combinations(nums, 3)]
    
    answer = 0
    for i in sums:
        isPrime = is_Prime(i)
        if isPrime:
            answer += 1

    return answer