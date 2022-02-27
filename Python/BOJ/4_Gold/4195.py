# 친구 네트워크
import sys
input = sys.stdin.readline


def find_head(num):
    if num != head[num]:
        head[num] = find_head(head[num])
    return head[num]


def union(num1, num2):
    head1 = find_head(num1)
    head2 = find_head(num2)
    if head1 == head2:
        return
    group_cnt[head1] += group_cnt[head2]
    group_cnt[head2] = 0
    head[head2] = head1


def get_idx(name):
    global idx
    if not name_dict.get(name):
        name_dict[name] = idx
        idx += 1
    return name_dict[name]


T = int(input())
result = []
for _ in range(T):
    F = int(input())

    head = list(range(2*(F+1)))
    group_cnt = [1]*(2*(F+1))
    name_dict = dict()
    idx = 1
    for f in range(F):
        n1, n2 = input().split()
        idx1 = get_idx(n1)
        idx2 = get_idx(n2)
        union(idx1, idx2)
        result.append(group_cnt[find_head(idx1)])
print(*result, sep='\n')
