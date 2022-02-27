# 시험 감독

import sys, math

input = sys.stdin.readline

N = int(input())
students = list(map(int, input().split()))
main_suprevisor, sub_supervisor = map(int, input().split())

cnt = 0
for student in students:
    student -= main_suprevisor
    cnt += 1
    if student <= 0:
        continue
    cnt += math.ceil(student/sub_supervisor)
    
print(cnt)