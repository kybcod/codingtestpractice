def solution(lottos, win_nums):
    answer=[]

    win_cnt = 0
    for i in lottos:
        if i in win_nums:
            win_cnt += 1

    zero_cnt = lottos.count(0)

    cnt = [win_cnt, zero_cnt + win_cnt ]

    for i in cnt:
        rank = 6 - i + 1
        if rank > 6 : rank = 6
        answer.append(rank)
    return sorted(answer)