def solution(lottos, win_nums):
    
# for lotto_number in lottos:
#     for win in win_nums:
#         if lotto_number == win:
#             matched_count += 1
    
    matched_count = len(set(lottos) & set(win_nums))
    unknown_count = lottos.count(0)
    highest_rank = min(7 - (matched_count + unknown_count), 6)
    lowest_rank = min(7 - matched_count, 6)

    return [highest_rank, lowest_rank]