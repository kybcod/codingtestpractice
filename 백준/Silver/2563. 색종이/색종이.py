n = int(input())
xylist =[ [0 for i in range(101)] for i in range(101)]
for i in range(n):
    x,y=map(int,input().split())
    for j in range(10):
        for k in range(10):
            xylist[x+j][y+k]=1
count=0  
for i in xylist:
    for j in i:
        if j==1:
            count+=1
print(count)

