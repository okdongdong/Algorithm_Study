import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
edges = {i: set() for i in range(N)}
additional_node = {i: {} for i in range(N)}

for i in range(N):
    edge_cnt = sum(arr[i])
    if edge_cnt % 2:
        print(-1)
        sys.exit()

    for j in range(i+1, N):
        if arr[i][j] > 2:
            additional_node[i][j] = (arr[i][j]-1) // 2

        if arr[i][j] % 2:
            arr[i][j] = 1
            arr[j][i] = 1

        else:
            arr[i][j] = 2
            arr[j][i] = 2

        edges[i].add(j)
        edges[j].add(i)


result = []


def dfs(s_node):
    for n_node in edges[s_node]:
        if arr[s_node][n_node]:

            arr[s_node][n_node] -= 1
            arr[n_node][s_node] -= 1
            dfs(n_node)

    result.append(s_node)


dfs(0)

for i in result:
    print(i+1, end=' ')
    if additional_node.get(i):
        for j, cnt in additional_node[i].items():
            print(f'{j+1} {i+1} '*cnt, end='')
        del additional_node[i]

# https://velog.io/@suker80/P5BaekjoonPython-1199-%EC%98%A4%EC%9D%BC%EB%9F%AC-%ED%9A%8C%EB%A1%9C
