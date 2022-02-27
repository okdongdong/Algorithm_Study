def beer(path):

    start = path.pop()
    end = path[0]
    next_store = [start]  # 시작점을 다음 방문지점으로 지정
    visited_store = []    # 한번 방문한 편의점을 다시 오지 않기 위해 리스트 생성

    while next_store:
        store = next_store.pop()        # 현재 방문하는 지점을 가져옴
        visited_store.append(store)     # 방문한 지점을 리스트에 추가  

        for i in path:
            if (abs(store[0] - i[0]) + abs(store[1] - i[1]) <= 1000) and (i not in visited_store):
                # 다음 지점과의 거리가 1000이하이고, 방문한 적이 없을 때
                next_store.append(i)    # 방문할 지점리스트에 추가

                if i == end:            # 다음 지점이 도착점일 때 happy반환
                    return 'happy'

    return 'sad'                        # 도착점에 도달하지 못할 때


T = int(input())
for _ in range(T):
    N = int(input())
    path = []
    for _ in range(N + 2):
        path.append(list(map(int, input().split())))
    print(beer(path))

