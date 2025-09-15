def solution(schedules, timelogs, startday):
    answer = 0
    employee = len(schedules)

    # 1. 출근 예정 시간을 분 단위로 변환하고 10분 지각 허용
    schedule_min = []
    for s in schedules:
        hour = s // 100
        minute = s % 100
        total_min = hour * 60 + minute + 10  # 10분 지각 허용
        schedule_min.append(total_min)

    # 2. 직원별 체크
    # startday: 1=월, 7=일
    startday = (startday - 1)  # 0=월, 6=일

    for idx in range(employee):
        logs = timelogs[idx]
        on_time = True
        for day in range(7):
            weekday = (startday + day) % 7  # 0=월, 6=일
            if weekday < 5:  # 평일
                log_time = (logs[day] // 100) * 60 + (logs[day] % 100)
                if log_time > schedule_min[idx]:
                    on_time = False
                    break
        if on_time:
            answer += 1

    return answer
