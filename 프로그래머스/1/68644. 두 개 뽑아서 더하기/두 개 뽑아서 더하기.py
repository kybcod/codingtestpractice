from itertools import combinations
def solution(numbers):
    sums = set()

    for i in combinations(numbers, 2):
        sums.add(sum(i))

    return sorted(sums)