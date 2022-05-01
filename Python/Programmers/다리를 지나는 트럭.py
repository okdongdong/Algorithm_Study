from collections import deque


def solution(bridge_length, weight, truck_weights):

    que = deque(truck_weights)
    on_bridge = deque([0]*bridge_length)
    time_cnt = 0
    temp = 0
    while que:
        time_cnt += 1
        temp -= on_bridge.popleft()

        if que[0] + temp <= weight:
            temp += que[0]
            on_bridge.append(que.popleft())
        else:
            on_bridge.append(0)

    return time_cnt + bridge_length


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100,	100, [10, 10, 10, 10, 10, 11, 10, 10, 10, 10]))
