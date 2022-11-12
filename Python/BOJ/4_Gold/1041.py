# 1면이 보이는 주사위 : 5n**2 - 16n + 12 개
# 2면이 보이는 주사위 : 8n - 12개
# 3면이 보이는 주사위 : 4개

N = int(input())
dice = list(map(int, input().split()))
if N == 1:
    result = sum(sorted(dice)[:5])
else:
    A, B, C, D, E, F = dice
    cases = [
        (A, B, C),
        (A, B, D),
        (A, C, E),
        (A, D, E),
        (B, C, F),
        (B, D, F),
        (C, E, F),
        (D, E, F),
    ]

    result = float("inf")
    for case in cases:
        a, b, c = sorted(case)
        result = min(
            (5 * N**2 - 16 * N + 12) * a + (8 * N - 12) * (a + b) + 4 * (a + b + c),
            result,
        )

print(result)
