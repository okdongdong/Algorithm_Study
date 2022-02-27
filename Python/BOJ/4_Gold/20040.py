# 사이클 게임
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find_head(num):
    if head[num] == num:
        return num
    head[num] = find_head(head[num])
    return head[num]


def union(num1, num2):
    head[find_head(num2)] = find_head(num1)


N, M = map(int, input().split())
head = list(range(N))
num_list = [list(map(int, input().split())) for _ in range(M)]
for i in range(M):
    num1, num2 = num_list[i]

    if find_head(num1) == find_head(num2):
        result = i+1
        break

    union(num1, num2)

else:
    result = 0

print(result)
