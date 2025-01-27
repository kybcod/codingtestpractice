def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    word = ''
    answer = ''
    i = 0

    while i < len(s):
        if s[i].isdigit(): 
            answer += s[i]
            i += 1
            continue

        word += s[i]  
        if word in words:  
            answer += str(words.index(word))
            word = ''  
        i += 1

    return int(answer)