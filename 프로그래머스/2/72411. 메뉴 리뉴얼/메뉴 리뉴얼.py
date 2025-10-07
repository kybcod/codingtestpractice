from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        comb_list = []
        
        for order in orders:
            order = sorted(order)
            comb_list += combinations(order,c)
    
        # 빈도수 계산
        counter = Counter(comb_list)

        if counter:
            max_count = max(counter.values())
            print(max_count)
            if max_count >= 2:
                for comb in counter: # key('A', 'C'): value4
                    if counter[comb] == max_count:
                        answer.append(''.join(comb))
    
    return sorted(answer) 