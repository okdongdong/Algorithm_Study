# # 축사 배정
# import sys
# sys.setrecursionlimit(100000)
#
#
# def assign_cow(cow):
#     for cow_wish in barn_wish[cow]:
#       if not check[cow_wish]:
#             check[cow_wish] = True
#             if barns[cow_wish] == -1 or assign_cow(barns[cow_wish]):
#                 barns[cow_wish] = cow
#                 return True
#     return False
#
#
# N, M = map(int, input().split())  # N: 소의 수, M: 축사의 수
# barn_wish = [list(map(int, input().split()))[1:] for _ in range(N)]
# barns = [-1] * (M + 1)
#
# cnt = 0
# for cow in range(N):
#     check = [False] * (M + 1)
#     if assign_cow(cow):
#         cnt += 1
#
# print(cnt)


# def assign_cow(cow):
#     for wish in barn_wish[cow]:
#         if check[wish]:
#             continue
#         check[wish] = True
#         if barns[wish] == -1 or assign_cow(barn[wish]):
#             barn[wish] = cow
#             return True
#     return False
#
# N, M = map(int, input().split())  # N: 소의 수, M: 축사의 수
# barn_wish = [list(map(int, input().split())) for _ in range(N)]
# barns = [-1] * (M + 1)
#
# for barn in barn_wish:
#     barn.pop(0)
#
# cnt = 0
# for cow in range(N):
#     check = [False] * (M + 1)
#     if assign_cow(cow):
#         cnt += 1
#
# print(cnt)

import sys

sys.setrecursionlimit(100000)


def assign_cow(cow):
    while barn_wish[cow]:
        cow_wish = barn_wish[cow].pop()
        if check[cow_wish]:
            continue
        if cow_wish == 0:
            return False
        if barns[cow_wish] == -1 or assign_cow(barns[cow_wish]):
            barns[cow_wish] = cow
            return True
    return False


N, M = map(int, input().split())  # N: 소의 수, M: 축사의 수
barn_wish = [list(map(int, input().split())) for _ in range(N)]
barns = [-1] * (M + 1)

for barn in barn_wish:
    barn.pop(0)

cnt = 0
for cow in range(N):
    check = [False] * (M + 1)
    if assign_cow(cow):
        cnt += 1

print(cnt)
