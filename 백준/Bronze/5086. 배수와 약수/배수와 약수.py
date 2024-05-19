# a가 b의 약수 (factor)
# a가 b의 배수 (multiple)
# a가 b의 약수,배수 아니다 (neither)

while True:
    a,b = map(int, input().split())
    if (a == 0 & b == 0):
        break
    if (b % a == 0):
        print("factor")
    if (a % b == 0):
        print("multiple")
    if (b % a != 0) & (a % b != 0):
        print("neither")