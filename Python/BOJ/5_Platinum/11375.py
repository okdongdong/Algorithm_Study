# 열혈강호
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def task_check(person):
    for task in people_task_list[person]:
        if not check[task]:
            check[task] = True
            if tasks[task]==-1 or task_check(tasks[task]):
                tasks[task] = person
                return True
    return False

N, M = map(int, input().split())
people_task_list = [list(map(int, input().split()))[1:] for _ in range(N)]
tasks = [-1] * (M+1)
cnt = 0
for person in range(N):
    check = [False] * (M+1)
    if task_check(person):
        cnt += 1

print(cnt)