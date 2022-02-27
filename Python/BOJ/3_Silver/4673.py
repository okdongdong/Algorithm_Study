def self_num(n):
    for i in str(n):
        n += int(i)
    return n

not_self = set()

for i in range(1,10001):
    not_self.add(self_num(i))

self_nums = sorted(list(set(range(1,10001)) - not_self))
print('\n'.join(map(str, self_nums)))
