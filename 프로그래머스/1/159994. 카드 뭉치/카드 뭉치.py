def solution(cards1, cards2, goal):
    for word in goal:
        if cards1 and cards1[0] == word:  # cards1의 첫 번째 단어가 goal과 같으면 제거
            cards1.pop(0)
        elif cards2 and cards2[0] == word:  # cards2의 첫 번째 단어가 goal과 같으면 제거
            cards2.pop(0)
        else:  # 둘 다 아니면 만들 수 없는 경우
            return "No"
    return "Yes"
