import sys
input = sys.stdin.readline


def comb(n=0, j=1):
    if n == 6:
        print(' '.join(map(str, selected)))
        return

    for i in range(j, len(nums)):
        selected.append(nums[i])
        comb(n+1, i+1)
        selected.pop()


flag = False
while True:
    nums = list(map(int, input().split()))

    if len(nums) == 1:
        break

    if flag:
        print()
    else:
        flag = True

    selected = []
    comb()
