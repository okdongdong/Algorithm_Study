import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [0]*N
ddd = {}
for i in range(N):
    temp = input().rstrip()
    arr[i] = temp
    ddd[temp] = i

result = []
for i in range(M):
    temp = input()
    try:
        temp2 = int(temp)
        result.append(arr[temp2-1])
    except:
        result.append(str(ddd[temp.rstrip()]+1))

print('\n'.join(result))
