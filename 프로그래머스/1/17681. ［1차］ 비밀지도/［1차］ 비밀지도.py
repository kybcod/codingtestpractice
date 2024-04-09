def solution(n, arr1, arr2):
    bins1 = []
    bins2 = []
    result = []
    answer = []

    for b in arr1:
        bins = bin(b)[2:]
        bins1.append(bins.zfill(n))

    for b in arr2:
        bins = bin(b)[2:]
        bins2.append(bins.zfill(n))

    # 둘 중 하나라도 벽이면 벽
    # 모두 공백이면 공백
    for i in range(len(bins1)):
        bit1 = int(bins1[i],2)
        bit2 = int(bins2[i],2)

        max_bin = bin(bit1 | bit2)[2:].zfill(n)  # 두 이진수를 비트별로 OR 연산하여 최댓값 구함
        temp_answer = ''
        for bit in max_bin:
            if bit == '1':
                temp_answer += "#"
            else:
                temp_answer += " "
        answer.append(temp_answer)
    return answer