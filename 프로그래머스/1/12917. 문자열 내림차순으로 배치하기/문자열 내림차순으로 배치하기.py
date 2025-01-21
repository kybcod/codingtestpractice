def solution(s):
    answer = ""
    s_list = sorted([i for i in s], reverse=True)
    for i in s_list:
        answer += i
    return (answer)