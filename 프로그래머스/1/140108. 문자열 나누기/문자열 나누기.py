def solution(s):
    answer = 0
    same = 0; diff=0

    for i in s:
        print(i)
        if same==diff:
            answer+=1
            k=i
            print("k", k)
            print("i", i)
        if k==i:
            same+=1
        else:
            diff+=1
    return answer