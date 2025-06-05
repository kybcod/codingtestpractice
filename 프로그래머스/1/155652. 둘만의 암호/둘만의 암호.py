def solution(s, skip, index):
    answer = ''
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in list(skip):
        alpha = alpha.replace(i,"")

    for s_word in s:
        answer += alpha[(alpha.find(s_word) + index) % len(alpha)]
    return answer