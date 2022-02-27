# 덱
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
deq = deque()
result = []
for _ in range(N):
    temp = input().split()
    a = temp[0]
    b = temp[-1]

    if a == 'push_back':
        deq.append(b)
    elif a == 'push_front':
        deq.appendleft(b)
    else:
        if deq:
            if a == 'pop_front':
                result.append(deq.popleft())
            elif a == 'pop_back':
                result.append(deq.pop())
            elif a == 'size': 
                result.append(str(len(deq)))
            elif a == 'empty':
                result.append('0')
            elif a == 'front':
                result.append(deq[0])
            elif a == 'back':
                result.append(deq[-1])
        else:
            if a == 'size':
                result.append('0')
            elif a == 'empty':
                result.append('1')
            else:
                result.append('-1')

print('\n'.join(result))
