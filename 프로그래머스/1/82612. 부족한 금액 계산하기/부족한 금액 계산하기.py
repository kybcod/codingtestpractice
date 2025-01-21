def solution(price, money, count):
    sum = 0
    for i in range(1, count+1):
        price_s = price * i
        sum += price_s
        
    if sum <= money:
        return 0
    else:
        return (sum-money)
     