# AC
from collections import deque

T = int(input())
results = []
for _ in range(T):
    p = input()
    n = int(input())
    try:
        nums = deque(map(int, input().lstrip('[').rstrip(']').split(',')))
    except:
        nums = deque()
    flag = True
    
    for cmd in p:
        if cmd == 'R':
            flag = not flag

        else:
            if not nums:
                result = 'error'
                break

            if flag:
                nums.popleft()
            
            else:
                nums.pop()

    else:
        if flag:
            result = '[' + ','.join(map(str, list(nums))) + ']'

        else:
            result = '[' + ','.join(map(str, list(nums)[::-1])) + ']'
    
    results.append(result)
print(*results, sep='\n')
