submitted = set(int(input()) for _ in range(28))
for student in range(1, 31):
    if student not in submitted:
        print(student)
