from itertools import combinations

nums = list(map(int, input().split()))
comb_list = combinations(nums, 3)
result = 987654321

for a, b, c in comb_list:
    temp_a, temp_b, temp_c = a, b, c

    while temp_c:
        temp_b, temp_c = temp_c, temp_b % temp_c

    b = b*c // temp_b
    temp_b = b

    while temp_b:
        temp_a, temp_b = temp_b, temp_a % temp_b

    result = min(result, (a*b) // temp_a)

print(result)
