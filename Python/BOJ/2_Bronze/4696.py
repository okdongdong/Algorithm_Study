import sys
input = sys.stdin.readline

while True:
    N = float(input())
    if N == 0:
        break
    result = 0
    for i in range(5):
        result += N**i
    print(f'{result:0.02f}')
