L = int(input())
nums = list(map(int, input().split()))
N = int(input())
nums.append(N)
nums.sort()

for idx, num in enumerate(nums):
    if num == N:
        N_idx = idx
        break

# N_idx == L이 될 수는 없음
if 0 < N_idx:
    left = nums[N_idx - 1]
    right = nums[N_idx + 1]

    result = (N-left)*(right-N) - 1

else:
    left = 0
    right = nums[N_idx + 1]
    result = (N-left)*(right-N) - 1

print(result if result > 0 else 0)
