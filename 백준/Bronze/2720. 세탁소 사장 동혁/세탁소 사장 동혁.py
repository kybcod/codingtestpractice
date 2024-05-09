q = 25
d = 10
n = 5
p = 1


t = int(input())
for _ in range(t):
    change_list = []
    a = int(input())
    change_list.append(a//q)
    a = a % q
    change_list.append(a//d)
    a = a % d
    change_list.append(a//n)
    a = a % n
    change_list.append(a//p)
    a = a%n
    print(*change_list)
    