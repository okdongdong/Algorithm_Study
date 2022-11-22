from itertools import product

N = input()
nums = list(product("47", repeat=len(N) - 1)) + list(product("47", repeat=len(N)))
temp = []
N = int(N)
for n in nums:
    num = int("".join(n) or 0)
    if N < num:
        continue
    temp.append(num)

print(max(temp))
