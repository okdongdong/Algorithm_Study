# 완전수
input()
nums = map(int, input().split())
result = []
for num in nums:
    num_sum = 1 if num > 1 else 0
    for n in range(2, int(num**.5)+1):
        if not num % n:
            num_sum += n
            if n != num//n:
                num_sum += num//n

    if num > num_sum:
        result.append("Deficient")
    elif num == num_sum:
        result.append("Perfect")
    else:
        result.append("Abundant")

print('\n'.join(result))
