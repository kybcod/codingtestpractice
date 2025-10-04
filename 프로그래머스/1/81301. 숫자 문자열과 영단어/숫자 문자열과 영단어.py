def solution(s):
    arr = ['zero','one', 'two', 'three','four','five','six','seven','eight','nine']
    answer = ''
    temp = ''
    
    for i in s:
        if i.isdigit():
            answer += i
        else:
            temp += i
            if temp in arr:
                answer += str(arr.index(temp))
                temp = ''
    
    return int(answer)
