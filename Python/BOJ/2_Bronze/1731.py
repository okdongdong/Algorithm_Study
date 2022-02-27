# 추론
N = int(input())
nums = [int(input()) for _ in range(N)]
a, b, c = nums[:3]
if a-b == b-c:
    print(nums[-1] + c-b)

else:
    print(nums[-1]*c//b)
