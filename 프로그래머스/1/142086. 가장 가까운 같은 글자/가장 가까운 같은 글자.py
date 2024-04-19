def solution(s):
    result = []  # 결과를 저장할 리스트
    seen = {}  # 이미 나온 문자와 그 위치를 저장하는 딕셔너리

    for i, char in enumerate(s):
        if char in seen:
            distance = i - seen[char]  # 현재 위치와 이미 나온 위치의 차이 계산
            result.append(distance)
        else:
            result.append(-1)
        
        seen[char] = i  # 현재 위치를 딕셔너리에 저장

    return result
