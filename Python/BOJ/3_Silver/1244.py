# 스위치 켜고 끄기

import sys
input = sys.stdin.readline

switch_N = int(input())     # on: 1, off: 0
switchs = list(map(int, input().split()))
student_N = int(input())    # 남학생 1, 여학생 2
students = [list(map(int, input().split())) for _ in range(student_N)]

for student in students:
    if student[0] == 1:
        for i in range(student[1]-1, switch_N, student[1]):
            switchs[i] = int(not switchs[i])
    else:
        i = student[1]-1
        switchs[i] = int(not switchs[i])
        n = 1
        while n <= i < switch_N-n:
            if switchs[i-n] != switchs[i+n]:
                break
            switchs[i-n] = int(not switchs[i-n])
            switchs[i+n] = int(not switchs[i+n])
            n += 1
        
for i in range(switch_N//20 + 1):
    print(*switchs[i*20:(i+1)*20])
    
