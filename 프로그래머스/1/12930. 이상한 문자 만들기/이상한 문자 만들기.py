def solution(s):
    answer = ''
    s_split = s.split(" ")
    for idx, s in enumerate(s_split):
        for i in range(len(s)):
            if i % 2 == 0:
                answer += s[i].upper()
            else:
                answer += s[i].lower()
        if idx != len(s_split) - 1:
            answer += " "
    return answer            