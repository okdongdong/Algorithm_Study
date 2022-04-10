def solution(bridge_length, weight, truck_weights):

    truck_weights.sort()
    left, right = 0, len(truck_weights)-1
    cnt = 0
    flag = True
    temp = 0
    while left <= right:
        if flag:
            right -= 1
            cnt += 1
            if temp + truck_weights[right] <= weight:
                flag = not flag
                temp += truck_weights[right]
            else:
                temp = 0

        else:
            if temp + truck_weights[left] <= weight:
                temp += truck_weights[left]
                left += 1
            else:
                temp = 0
                flag = not flag

    answer = len(truck_weights) + bridge_length * cnt

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100,	100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
