# 소수 쌍

def dfs(first_num, first_pair, num):
    if num in visited:
        return False

    visited.add(num)
    for num_pair in number_dict[num]:
        if num_pair == first_pair:
            continue

        if not connect.get(num_pair) or dfs(first_num, first_pair, connect.get(num_pair)):
            connect[num_pair] = num
            return True

    return False


N = int(input())
nums = list(map(int, input().split()))

prime = [True]*2001
prime[0], prime[1] = False, False

for i in range(2, int(2001**.5)+1):
    for j in range(i+i, 2001, i):
        if not prime[j]:
            continue

        prime[j] = False

number_dict = {}
group_a = []
group_b = []
standard = nums[0] % 2
for n in nums:
    if n % 2 == standard:
        group_a.append(n)
        number_dict[n] = []
    else:
        group_b.append(n)

for a in group_a:
    for b in group_b:
        if prime[a+b]:
            number_dict[a].append(b)

result = []
fist_num = nums[0]
for first_pair in number_dict[fist_num]:
    connect = {}
    for num in group_a:
        if num == fist_num:
            continue

        visited = set()
        dfs(fist_num, first_pair, num)

    if len(connect) == N//2-1:
        result.append(first_pair)

result.sort()

if result:
    print(*result)
else:
    print(-1)
