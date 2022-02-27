# 사탕개수 M(<=10**18)개 고정
# 모든 가방에서 종류 같아야
# 가방의 최대개수를 구하는 문제
# 한 가방에 들어가는 사탕의 종류별 숫자를 계산하여 풀이
# 이진 탐색 방법을 응용하여 접근

def Candy(N, M, nums):
    min_num = 1
    max_num = max(nums)

    while min_num <= max_num:
        mid_num = (min_num + max_num) // 2
        cnts = 0

        for num in nums:
            cnts += num // mid_num

        if cnts == M:   # 한 가방에 들어가는 사탕의 각 종류별 숫자를 알 수 있음
            result_nums = []
            for num in nums:
                if num//mid_num != 0:
                    result_nums.append(num//(num//mid_num))
            return min(result_nums)  # 종류별 숫자를 계산하여 최솟값 반환

        elif cnts <= M:
            max_num = mid_num - 1

        else:
            min_num = mid_num + 1

    return max_num


T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    nums = [int(i) for i in input().split()]
    result = Candy(N, M, nums)
    print(f'#{t+1} {result}')


## 아래는 가방에 들어가는 사탕을 하나씩 늘리는 방식 => 시간초과

# T = int(input())
#
# for t in range(T):
#     N, M = map(int, input().split())
#     nums = [int(i) for i in input().split()]
#     if N == 1:
#         result = nums[0]//M
#
#     else:
#         temp_nums = [i for i in nums]
#         Q = max(nums)//min(nums)
#         if Q < N:
#             cnt_nums = [num//min(nums) for num in nums]
#         else:
#             cnt_nums = [0] * N
#
#         while sum(cnt_nums) < M:
#
#             max_index = temp_nums.index(max(temp_nums))
#             min_index = temp_nums.index(min(temp_nums))
#             cnt_nums[max_index] += 1
#
#             try:
#                 temp_nums[max_index] = nums[max_index]/cnt_nums[max_index]
#                 if temp_nums[max_index] < temp_nums[min_index]:
#                     cnt_nums[max_index] -= 1
#                     max_index = temp_nums.index(max(temp_nums))
#                     cnt_nums[max_index] += 1
#
#             except:
#                 pass
#
#         result_nums = []
#
#         for n in range(N):
#             try:
#                 result_nums.append(nums[n]//cnt_nums[n])
#             except:
#                 pass
#
#         result = min(result_nums)
#     print(f'#{t+1} {result}')
