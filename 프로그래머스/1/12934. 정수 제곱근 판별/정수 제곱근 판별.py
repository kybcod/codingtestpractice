import math
def solution(n):
    for i in range(1,int(math.sqrt(n))+1):
        if i == math.sqrt(n):
            answer = (i + 1) * (i+1)
        else:
            answer = -1
    return answer