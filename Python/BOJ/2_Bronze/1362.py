results = [":-(", ":-)"]


def case_check(o, w):
    is_dead = False
    while True:
        action, n = input().split()
        if w <= 0:
            is_dead = True

        if action == "F":
            w += int(n)

        elif action == "E":
            w -= int(n)

        else:
            return "RIP" if is_dead else results[(0.5 * o < w < 2 * o)]


num = 1
while True:
    o, w = map(int, input().split())
    if o == w == 0:
        break
    print(num, case_check(o, w))
    num += 1
