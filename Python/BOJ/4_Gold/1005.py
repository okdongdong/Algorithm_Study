import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def DFS(_pre):
    global stack
    if visited[_pre]:
        return

    for next in tech_tree[_pre]:
        DFS(next)
        visited[next] = True
        stack.append((_pre, next))


T = int(input())
result = []
for _ in range(T):
    N, K = map(int, input().split())
    build_time_list = [0] + list(map(int, input().split()))
    total_build_time = build_time_list[:]
    rules = [list(map(int, input().split())) for _ in range(K)]
    tech_tree = [[] for _ in range(N+1)]
    W = int(input())
    visited = [False] * (N+1)
    stack = []
    for pre, next in rules:
        tech_tree[pre].append(next)

    for i in range(1, N+1):
        DFS(i)

    for pre, next in stack[::-1]:
        build_time = total_build_time[pre] + build_time_list[next]
        total_build_time[next] = max(build_time, total_build_time[next])

    result.append(total_build_time[W])
    print(stack)
print(*result, sep='\n')

# def TechTime(n):    # 재귀, 시간초과..
#     if memo[n]:
#         return memo[n]

#     if tech_tree[n]:
#         lst = []
#         for i in tech_tree[n]:
#             lst.append(TechTime(i))

#         memo[n] = build_time[n-1] + max(lst)
#         return memo[n]

#     memo[n] = build_time[n-1]
#     return memo[n]


# T = int(input())
# for tc in range(T):

#     N, K = map(int, input().split())
#     build_time = list(map(int, input().split()))
#     rules = [map(int, input().split()) for _ in range(K)]
#     W = int(input())    # 완료해야할 건물 번호
#     memo = [0]*(N+1)
#     tech_tree = [[] for _ in range(N+1)]

#     # 최종테크부터 거꾸로 내려감
#     for r, c in rules:
#         tech_tree[c].append(r)

#     print(TechTime(W))
