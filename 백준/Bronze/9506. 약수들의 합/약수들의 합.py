while True:
    n = int(input())
    if (n == -1):
        break
    
    i_list = []
    for i in range(1,n):
        if (n % i == 0):
            i_list.append(i)
    if sum(i_list) == n:
        print(n, "=",end=" ")
        print(*i_list, sep=" + ")
    else:
        print(n,"is NOT perfect.")
