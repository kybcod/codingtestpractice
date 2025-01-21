def solution(t, p):
    cnt = 0
    p_length = len(p)
    p_value = int(p)

    for i in range(len(t) - p_length + 1):
        substring = int(t[i:i + p_length])
        if substring <= p_value:
            cnt += 1

    return (cnt)