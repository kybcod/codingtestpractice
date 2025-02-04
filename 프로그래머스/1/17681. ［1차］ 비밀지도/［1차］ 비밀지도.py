def solution(n, arr1, arr2):
    arr1_2=[]
    arr2_2=[]

    #이진법 함수
    def binary(a, n):
        ternary = ""
        while a > 0:
            a, remaider = divmod(a, 2)
            ternary += str(remaider)
        return ternary[::-1].zfill(n)

    # 1. 이진법으로 변경
    for i in arr1:
        arr1_2.append(binary(i, n))
    for i in arr2:
        arr2_2.append(binary(i, n))

    # 2. arr1과 arr2를 합하기
    sums = []
    for i in range(len(arr1_2)):
        sums.append("".join("1" if a == "1" or b == "1" else "0" for a, b in zip(arr1_2[i], arr2_2[i])))


    # 2. 0은 공백, 1이상은 #으로 변경
    answer = []
    st = ""
    for i in sums:
        st = ""  # 문자열 초기화
        for j in i:
            st += "#" if j != "0" else " "  
        answer.append(st)
    return answer