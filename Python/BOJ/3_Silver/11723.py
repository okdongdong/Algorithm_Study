import sys

input = sys.stdin.readline

N = int(input())
S = set()
ALL = list(map(str, range(1, 21)))
for _ in range(N):
    cmd = input().split()

    if cmd[0] == "add":
        S.add(cmd[1])

    elif cmd[0] == "remove":
        S.discard(cmd[1])

    elif cmd[0] == "check":
        print(int(cmd[1] in S))

    elif cmd[0] == "toggle":
        if cmd[1] in S:
            S.discard(cmd[1])
        else:
            S.add(cmd[1])

    elif cmd[0] == "all":
        S = set(ALL)

    elif cmd[0] == "empty":
        S.clear()
