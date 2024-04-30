# 등급에 따른 과목평점을 딕셔너리로 저장합니다.
grade_points = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

# 입력 받기
subjects = []
for _ in range(20):
    subject, credit, grade = input().split()
    subjects.append((subject, float(credit), grade))

# 전공 평점 계산
total_credit = 0
total_grade_point = 0
for subject, credit, grade in subjects:
    if grade != 'P':  # 등급이 P가 아닌 경우에만 고려합니다.
        total_credit += credit
        total_grade_point += credit * grade_points[grade]

# 전공 평점 출력
if total_credit == 0:
    print("0.000000")  # 총 학점이 0인 경우
else:
    gpa = total_grade_point / total_credit
    print(f"{gpa:.6f}")
