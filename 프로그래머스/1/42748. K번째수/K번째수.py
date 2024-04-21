def solution(array, commands):
    answer = []
    for arr in commands:
        i, j, k = arr
        sub_array = sorted(array[i-1:j])
        answer.append(sub_array[k-1])
    return answer