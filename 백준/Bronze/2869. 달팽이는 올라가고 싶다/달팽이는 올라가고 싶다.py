# (A−B)×(날짜)+B=V : v−b를 사용하여 하루 동안 올라가야 할 실제 남은 거리
import math
a,b,v = map(int, input().split())
day = (v-b)/(a-b)
print(math.ceil(day))