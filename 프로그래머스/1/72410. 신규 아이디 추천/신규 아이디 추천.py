import re

def solution(new_id):
    
    new_id = new_id.lower() # 1단계: 소문자 치환
    new_id = re.sub(r'[^a-z0-9\-_.]', '', new_id) # 2단계: 허용 문자 제외 제거
    new_id = re.sub(r'\.+', '.', new_id) # 3단계: 마침표 2번 이상 → 하나로
    new_id = new_id.strip('.') # 4단계: 처음/끝 마침표 제거
    
    if not new_id: # 5단계: 빈 문자열이면 'a'
        new_id = 'a'
    
    new_id = new_id[:15].rstrip('.') # 6단계: 16자 이상이면 자르고, 끝이 '.'이면 제거

    while len(new_id) < 3: # 7단계: 길이 2 이하면, 마지막 문자 반복해서 3자 만들기
        new_id += new_id[-1]

    return new_id
