a,b,c,d,e,f = map(int, input().split())
answer = [0]*6

if a != 1:
    answer[0] = 1-a
    
if b != 1:
    answer[1] = 1-b

if c != 2:
    answer[2] = 2-c

if d != 2:
    answer[3] = 2-d
        
if e != 2:
    answer[4] = 2-e

if f != 8:
    answer[5] = 8-f
        
print(*answer)