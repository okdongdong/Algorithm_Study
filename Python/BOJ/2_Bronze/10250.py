T = int(input())
for tc in range(T):
    H,W,N = map(int,input().split())
    print(f'{N%H if N%H else H}{N//H + 1 if N%H else N//H:02.0f}')
    