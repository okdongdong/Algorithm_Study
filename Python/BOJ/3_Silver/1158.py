N, K = map(int, input().split())

nums = [i+1 for i in range(N)]
result = []
i = K
n = 0

while True:
    if i < 1:
        i += N

    result.append(nums.pop(i-1))
    i += K - 1
    N -= 1

    if N == 0:
        break

    if i > N:
        i = i % N

print('<', end='')
print(*result, sep=', ', end='')
print('>')

# print(nums)

# for _ in range(N):
#     if i in result:
#         i
#     else:
#         result.append(i)

# while True:    # 모든 숫자를 사용하면 탈출
#     j = 1           # j : 사용하지 않은 숫자 카운트
#     while True:
#         if nums[i - 1]:     # 사용하지 않은 숫자를 만난 경우
#             if j == K:      # 사용하지 않은 숫자 중 K번째 숫자를 만났을 때
#                 n += 1
#                 nums[i-1] = False        # 사용한 숫자 False
#                 result.append(str(i))    # 결과리스트에 추가, 결과를 쉽게 출력하기 위해 str 사용
#                 break
#             j += 1      # 사용하지 않은 숫자 카운트 증가
#         i += 1          # 전체 탐색 인덱스 층가
#         if i > N:       # 숫자가 리스트의 길이보다 커질경우 초기화
#             i = 1
#     if n >= N:
#         break
