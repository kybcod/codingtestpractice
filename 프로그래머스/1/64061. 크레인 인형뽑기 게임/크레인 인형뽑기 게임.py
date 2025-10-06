def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves:
        for row in board:
            if row[move - 1] != 0:
                doll = row[move - 1] # 인형뽑이
                row[move - 1] = 0 # 뽑으면 0으로 변경
                
                if basket and basket[-1] == doll: # 뽑은 인형 basket에 마지막 인형으로 같은지 확인
                    basket.pop() # 같다면 이미 basket에 있던 인형 빼기
                    answer += 2
                else:
                    basket.append(doll) # 아니면 넣기
                break # 이미 인형을 뽑으면 이 줄은 더 이상 뽑으면 안됨
    
    return answer