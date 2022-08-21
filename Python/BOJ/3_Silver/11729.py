def recur(n, start=1, end=3):
    global cnt
    cnt += 1

    if n == 1:
        move.append(f'{start} {end}')
        return

    target = 6-start-end

    recur(n-1, start, target)
    move.append(f'{start} {end}')
    recur(n-1, target, end)


N = int(input())
cnt = 0
move = []
recur(N)
print(cnt)
print('\n'.join(move))
