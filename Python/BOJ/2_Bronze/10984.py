import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    total_C = 0
    total_G = 0
    for i in range(N):
        c, g = map(float, input().split())
        total_C += c
        total_G += g*c

    print(int(total_C), round(total_G/total_C, 1))
