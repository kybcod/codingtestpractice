def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    #전부다 초로 바꾸고
    vl = chSec(video_len)
    ps = chSec(pos)
    op_st = chSec(op_start)
    op_e = chSec(op_end)
    
    # 오프닝 구간(op_start ≤ 현재 재생 위치 ≤ op_end)인 경우 자동으로 오프닝이 끝나는 위치
    ps = op_e if op_st <= ps <= op_e else ps
    
    for c in commands:
        
        # prev일 때 pos가 10초 이하이면 pos = 0 그렇지 않으면 -10
        if c == "prev":
            ps = 0 if ps < 10 else ps - 10
        # next일 때 video_len - pos가 10초 미만이면 pos는 video_len 그렇지 않으면 + 10
        elif c == "next":
            ps = vl if vl - ps < 10 else ps + 10

        ps = op_e if op_st <= ps <= op_e else ps
        
    return toTimeStr(ps)


# 초로 바꾸는 함수  # 780
def chSec(time_str):
    min, sec = time_str.split(":")
    ch_sec = int(min) * 60 + int(sec)
    return ch_sec


# 분:초로 변환
def toTimeStr(seconds):
    m = seconds // 60
    s = seconds % 60
    return f"{m:02d}:{s:02d}"

