def is_powerful(i, j):
    power = (j-i)*(abs(stone[i] - stone[j]) + 1)
    if power > K:
        return False

    return True


N, K = map(int, input().split())
stone = list(map(int, input().split()))
possible = [True]*N

for j in range(1, N):
    for i in range(max(j-1000, 0), j):
        if not possible[i]:
            continue

        if is_powerful(i, j):
            break

    else:
        possible[j] = False

print('YES' if possible[-1] else 'NO')


# 시간초과
# def small():
#     stone = [1]

#     while stone:
#         s = stone.pop()
#         for i in range(s+1, N+1):
#             if K >= (i-s)*(1+abs(A[s-1]-A[i-1])):
#                 stone.append(i)

#         if N in stone:
#             return 'YES'

#     return 'NO'

# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# print(small())
