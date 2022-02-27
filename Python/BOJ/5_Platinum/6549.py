import sys

input = sys.stdin.readline

while True:
    histogram = list(map(int, input().split()))
    if histogram[0] == 0:
        break
    N = histogram[0]
    histogram[0] = 0

    histogram += [0]
    pre_height_idx = 0
    pre_height_idx_stack = [0]
    width_list = [0] * (N + 2)

    # 직사각형의 너비 판별
    for i in range(len(histogram)-1):
        if histogram[i] > histogram[i + 1]:
            while True:
                if histogram[i+1] < histogram[pre_height_idx_stack[-1]]:
                    pre_height_idx = pre_height_idx_stack.pop()
                    width_list[pre_height_idx] = i - pre_height_idx_stack[-1]
                else:
                    break

        pre_height_idx_stack.append(i+1)

    # 넓이 계산
    max_area = 0
    for i in range(N+2):
        area = width_list[i] * histogram[i]
        if max_area < area:
            max_area = area

    print(max_area)

    # print('# height: ',histogram)
    # print('# width: ',width_list)
    # print('# area: ',max_area)
