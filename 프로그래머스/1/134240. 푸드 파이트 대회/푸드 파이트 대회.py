def solution(food):
    result = ''
    answer = ''
    for idx, count in enumerate(food[1:]):
        result += str(idx+1) * (count//2)
        
    answer = result + str(food.index(1)) + result[::-1]
    return answer