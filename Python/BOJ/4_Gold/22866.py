# 탑 보기
N = int(input())
height = list(map(int, input().split()))
cnt_list = [0] * N
near_list = [(987654321, 987654321)] * N     # dist, idx

left_stack = []
right_stack = []

for i in range(N):
    while left_stack and left_stack[-1][1] <= height[i]:
        left_stack.pop()

    cnt_list[i] += len(left_stack)

    if left_stack and i != left_stack[-1][0]:
        near_list[i] = min(
            (abs(i-left_stack[-1][0]), left_stack[-1][0]+1), near_list[i])

    left_stack.append((i, height[i]))

    j = -i-1
    while right_stack and right_stack[-1][1] <= height[j]:
        right_stack.pop()
    if right_stack and right_stack[-1][0] != j:
        near_list[j] = min((abs(right_stack[-1][0] - j), N +
                            right_stack[-1][0]+1), near_list[j])
    cnt_list[j] += len(right_stack)

    right_stack.append((j, height[j]))

result = []
for i in range(N):
    if cnt_list[i]:
        result.append(f'{cnt_list[i]} {near_list[i][1]}')
    else:
        result.append('0')

print('\n'.join(result))
