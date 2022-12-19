N = int(input())
cmds = [input().split() for _ in range(N)]
stack = []
t = float("inf")
for i in range(N - 1, -1, -1):
    cmd, a, b = cmds[i]
    if int(b) >= t:
        continue

    if cmd == "undo":
        a, b = map(int, (a, b))
        t = b - a

    else:
        stack.append(a)

print("".join(stack[::-1]))
