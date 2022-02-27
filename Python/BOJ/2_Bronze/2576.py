# import sys
# nums = sys.stdin.readlines()
nums = [int(input()) for _ in range(7)]

result = []
for num in nums:
    if num%2:
        result.append(num)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)

