# 입력 받기
N = int(input())
words = [input() for _ in range(N)]

# 그룹 단어 판별 함수 정의
def is_group_word(word):
    checked = []
    prev_char = None
    for char in word:
        if char in checked:  # 이미 등장한 문자인 경우
            if prev_char != char:  # 이전 문자와 다르면 그룹 단어가 아님
                return False
        else:  # 처음 등장하는 문자인 경우
            checked.append(char)
        prev_char = char
    return True

# 그룹 단어 개수 세기
group_word_count = 0
for word in words:
    if is_group_word(word):
        group_word_count += 1

# 결과 출력
print(group_word_count)
