def solution(numbers):
    answer = 0
    number = sorted(numbers)
    for i in range(len(number)):
        answer = number[i] * number[i-1]
    return answer