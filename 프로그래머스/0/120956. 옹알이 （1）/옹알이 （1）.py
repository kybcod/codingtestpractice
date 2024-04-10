def solution(babbling):
    # 조카의 발음을 나타내는 딕셔너리
    pronunciation = {
        "aya": 1,
        "ye": 1,
        "woo": 1,
        "ma": 1
    }
    
    # 발음 가능한 단어의 개수를 저장할 변수
    word_count = 0
    
    # babbling 배열을 순회하며 발음 가능한 단어를 찾음
    for word in babbling:
        i = 0
        while i < len(word):
            found = False
            for pron in pronunciation:
                if word.startswith(pron, i):
                    found = True
                    i += len(pron)
                    break
            if not found:
                break
        
        # 모든 발음이 가능한 경우 단어 개수를 증가
        if i == len(word):
            word_count += 1
    
    return word_count

