def solution(record):
    answer = []
    usernames = dict()
    actions = []
    
    for line in record:
        parts = line.split()
        action = parts[0]
        uid = parts[1]
        name = parts[2] if len(parts) == 3 else None

        if action in ("Enter", "Change"):
            usernames[uid] = name  # 최신 닉네임 저장

        if action in ("Enter", "Leave"):
            actions.append((action, uid))  # 나중에 메시지 생성용

    # 메시지 생성
    for action, uid in actions:
        nickname = usernames[uid]
        if action == "Enter":
            answer.append(f"{nickname}님이 들어왔습니다.")
        else:
            answer.append(f"{nickname}님이 나갔습니다.")
        
    
    return answer