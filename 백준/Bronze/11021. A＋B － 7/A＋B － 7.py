n = int(input()) #Test case
for i in range(1, n+1):
        a,b = map(int, input().split())
        print("Case #"+ str(i) + ": " + str(a+b))