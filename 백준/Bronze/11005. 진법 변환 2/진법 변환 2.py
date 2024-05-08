n,b = map(int, input().split())
array = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string = ''

while n:
    string += str(array[n%b])
    n //= b

print(string[::-1])
