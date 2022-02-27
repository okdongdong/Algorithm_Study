# 날카로운 눈

# 누적합을 이용한 이분탐색

import sys

input = sys.stdin.readline


def cal_sum(num):
    temp = 0
    for a, b, c in nums:
        if a <= num:
            temp += (min(b, num) - a)//c + 1
    return temp


N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
left, right = 1, 2147483647

if not cal_sum(right) % 2:
    result = ['NOTHING']

else:
    while left < right:
        mid = (left + right)//2
        if cal_sum(mid) % 2:
            right = mid
        else:
            left = mid + 1
    result = [left, cal_sum(left) - cal_sum(left-1)]

print(*result)
