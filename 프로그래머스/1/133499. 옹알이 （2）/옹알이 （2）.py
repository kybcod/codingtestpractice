def solution(babbling):
    word = ["aya", "ye", "woo", "ma"]
    cnt = 0

    for i in babbling:
        for j in word:
            
            # 단어가 연속으로 두 번 이상 나오지 않으면
            if j * 2 not in i:
                i = i.replace(j," ") #해당 단어를 해당 문자열에 제거
                
        # 문자열이 공백이 되면 모든 단어가 제거 후 cnt +1   
        if i.strip() == "":
            cnt += 1
    return cnt