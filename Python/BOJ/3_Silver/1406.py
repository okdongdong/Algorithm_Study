# 에디터
import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []
N = int(input())
for _ in range(N):
    now_input = input().rstrip()
    if now_input == 'L':
        if left:
            right.append(left.pop())

    elif now_input == 'D':
        if right:
            left.append(right.pop())

    elif now_input == 'B':
        if left:
            left.pop()

    else:
        char = now_input.split()[1]
        left.append(char)

result = ''.join(left) + ''.join(right[::-1])

print(result)
