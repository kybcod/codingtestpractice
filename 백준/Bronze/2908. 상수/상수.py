n1, n2 = map(str, input().split())

answer = n1[::-1] if n1[::-1] > n2[::-1] else n2[::-1]
print(answer)