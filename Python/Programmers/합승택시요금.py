def solution(n, s, a, b, fares):
    INF = 987654321
    cost_list = [INF]*(n+1)

    road = [[] for _ in range(n+1)]
    for st, ed, cost in fares:
        road[st].append((ed, cost))
        road[ed].append((st, cost))


    # A, B가 따로 가는경우
    # S -> A

    여기서 다익스트라로 조지구요

    # S -> B

    여기서도 조집니다

    두개를 합치고
    


    # A, B가 같이 가는경우
    여기랑 비교해서 출력해야대요


    return result