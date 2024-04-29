s = input()
alpha_list = [-1] * 26

for idx, ch in enumerate(s):
    alpha_index = ord(ch)-ord('a')
    if alpha_list[alpha_index] == -1:
        alpha_list[alpha_index] = idx
print(*alpha_list)

# 알파벳 인덱스 찾기 : ord('')-ord('a')