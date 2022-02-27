# 부호

import sys
input = sys.stdin.readline

for tc in range(3):
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    sum_nums = sum(nums)
    if sum_nums > 0:
        print('+')
    elif sum_nums < 0:
        print('-')
    else:
        print(0)
