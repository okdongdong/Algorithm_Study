import sys
input = sys.stdin.readline

N = int(input())
result = []
while True:
    num = int(input())
    if not num:
        break

    if num % N:
        result.append(f'{num} is NOT a multiple of {N}.')
    else:
        result.append(f'{num} is a multiple of {N}.')

print('\n'.join(result))
