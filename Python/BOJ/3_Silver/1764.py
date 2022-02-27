import sys

N, M = map(int, input().split())
name = sys.stdin.read().splitlines()
n_lst = set(name[:N])
m_lst = set(name[N:])

result = sorted(list(n_lst & m_lst))

print(len(result), *result, sep='\n')
