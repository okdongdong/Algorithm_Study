import pprint

import sys

input = sys.stdin.readline

N, x = map(int, input().split())

pipes = [tuple(map(int, input().split())) for _ in range(N)]

# 길이별로 만들 수 있는 모든 경우의 수를 구함
pipe_length_arr = [[0]*(x+1) for _ in range(N)]
for idx, (length, cnt) in enumerate(pipes):
    for i in range(1, cnt+1):
        try:
            pipe_length_arr[idx][length*i] = 1
        
        except:
            pass

for r in range(1, N):
    for c in range(x+1):
        for i in range(pipes[r][1] + 1):
            if c - pipes[r][0]*i > 0:
                pipe_length_arr[r][c] += pipe_length_arr[r - 1][c - pipes[r][0]*i]
            

print(pipe_length_arr[-1][-1])

pprint.pprint(pipe_length_arr)





# # 완전 탐색

# import sys
# input = sys.stdin.readline

# N, x = map(int, input().split())

# pipes = [tuple(map(int, input().split())) for _ in range(N)]

# # 길이별로 만들 수 있는 모든 경우의 수를 구함
# pipe_lengths_list = []
# for length, cnt in pipes:
#     temp = []
#     for i in range(cnt+1):
#         temp.append(length*i)
#     pipe_lengths_list.append(temp)

# cnt_list = [0] * N
# cnt_list[0] += 1
# result = 0

# while cnt_list[-1] <= pipes[-1][1]:
#     temp_sum = 0
#     for i in range(N):
#         temp_sum += pipe_lengths_list[i][cnt_list[i]]
#         if temp_sum > x:
#             break
#     else:
#         if temp_sum == x:
#             result += 1

#     cnt_list[0] += 1
#     for i in range(N-1):
#         if cnt_list[i] > pipes[i][1]:
#             cnt_list[i] = 0
#             cnt_list[i+1] += 1

# print(result)
