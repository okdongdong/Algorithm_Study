# 친구
N = int(input())
arr = [input() for _ in range(N)]
friends = [set() for _ in range(N)]
for i in range(N-1):
    for j in range(i+1, N):
        if arr[i][j] == 'Y':
            friends[i].add(j)
            friends[j].add(i)

friends_2 = [set() for _ in range(N)]
max_cnt = 0

for i in range(N):
    friends_2[i] |= friends[i]
    for j in friends[i]:
        friends_2[i] |= friends[j]

    friends_2[i].discard(i)
    max_cnt = max(max_cnt, len(friends_2[i]))

print(max_cnt)
