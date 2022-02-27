# 공장
import math

def update(idx):
    while idx < len(tree):
        tree[idx] += 1
        idx += (idx & -idx)


def cnt_sum(idx):
    cnt = 0
    while idx > 0:
        cnt += tree[idx]
        idx -= idx & -idx
    return cnt


N = int(input())
num1 = input().split()
num2 = input().split()
tree = [0] * ((1 << math.ceil(math.log2(N))) + 1)  # N보다 큰 가장 작은 2**n
order_dict = dict()

for i in range(N):
    order_dict[num2[i]] = i+1

cnt = 0

for num in num1:
    idx = order_dict[num]
    update(idx)
    cnt += tree[-1] - cnt_sum(idx)

print(cnt)
