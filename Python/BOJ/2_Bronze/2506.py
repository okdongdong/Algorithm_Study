# 점수계산
N = int(input())
nums = list(map(int, input().split()))
result, temp = 0, 0

for num in nums:
    if num:
        temp += 1
    else:
        temp = 0

    result += temp

print(result)
