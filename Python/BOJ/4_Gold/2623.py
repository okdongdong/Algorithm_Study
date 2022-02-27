# 음악프로그램 
N, M = map(int,input().split())
pre_singer_set_list = [set() for _ in range(N+1)]
next_singer_set_list = [set() for _ in range(N+1)]

for _ in range(M):
    singer = list(map(int, input().split()))
    for i in range(2, singer[0]+1):
        for j in range(1, i):
            pre_singer_set_list[singer[i]].add(singer[j])
            next_singer_set_list[singer[j]].add(singer[i])

now_member_list = []
for i in range(1, N+1):
    if len(pre_singer_set_list[i]) == 0:
        now_member_list.append(i)

idx = 0
while idx < len(now_member_list):
    now_member = now_member_list[idx]
    for next_member in next_singer_set_list[now_member]:
        pre_singer_set_list[next_member].remove(now_member)
        if not pre_singer_set_list[next_member]:
            now_member_list.append(next_member)
    idx += 1

if idx == N:
    print(*now_member_list, sep='\n')

else:
    print(0)