# 구간 곱 구하기

import sys
import math
input = sys.stdin.readline


def create(idx, s, e):
    if s == e:
        tree[idx] = nums[s]
    else:
        mid = (s+e)//2
        tree[idx] = create(idx*2, s, mid) * create(idx*2+1, mid+1, e) % 1000000007
    return tree[idx]


def update(idx, t, v, s, e):
    if t < s or e < t:
        return

    if s == e:
        tree[idx] = v
        return

    mid = (s+e)//2
    update(idx*2, t, v, s, mid)
    update(idx*2+1, t, v, mid+1, e)

    tree[idx] = tree[idx*2]*tree[idx*2+1] % 1000000007


def cal(idx, l, r, s, e):
    if r < s or e < l:
        return 1

    if l <= s and e <= r:
        return tree[idx]

    mid = (s+e)//2
    return cal(idx*2, l, r, s, mid) * cal(idx*2+1, l, r, mid+1, e) % 1000000007


N, M, K = map(int, input().split())
nums = [0]+[int(input()) for _ in range(N)]
level = math.ceil(math.log2(N))
tree = [1]*(2**(level+1))
result = []
create(1, 1, N)
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, b, c, 1, N)
        nums[b] = c
    else:
        result.append(cal(1, b, c, 1, N))
print(*result, sep='\n')
