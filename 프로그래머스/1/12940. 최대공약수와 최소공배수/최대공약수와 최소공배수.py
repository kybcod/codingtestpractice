import math

def solution(a, b):
    gcd = math.gcd(a, b)  # 최대공약수
    lcm = (a * b) // gcd  # 최소공배수
    return [gcd, lcm]