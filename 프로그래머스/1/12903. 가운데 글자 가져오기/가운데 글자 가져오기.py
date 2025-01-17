def solution(s):
    s_list = [i for i in s]
    for i in range(len(s_list)):
        if len(s_list) % 2 != 0:
            if i == (len(s_list)//2):
                return (s_list[i])
        else:
            if i == (len(s_list)//2) - 1:
                return (s_list[i]+s_list[i+1])