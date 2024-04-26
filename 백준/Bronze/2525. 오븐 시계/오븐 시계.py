h,m = map(int, input().split())
c = int(input())
cm = c+m

print((h + (cm//60)) % 24, cm % 60)