# 나이순 정렬
import sys
input = sys.stdin.readline
N = int(input())
peoples = [input().split() + [i] for i in range(N)]
result = []
peoples.sort(key= lambda x:(int(x[0]), x[2]))
for people in peoples:
    result.append(' '.join(people[:2]))

print(*result, sep='\n')
