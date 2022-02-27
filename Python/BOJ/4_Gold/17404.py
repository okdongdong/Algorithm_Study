# RGB거리 2
import sys
input = sys.stdin.readline
N = int(input())
rgb_list = [list(map(int, input().split())) for _ in range(N)]
other_color_dict = {
    0: (1, 2),
    1: (0, 2),
    2: (0, 1),
}

# dp
dp = [[0, 0, 0] for _ in range(N)]    # [r, g, b]
min_result = 1000001
for first_color in [0, 1, 2]:
    dp[0][first_color] = rgb_list[0][first_color]
    for color in other_color_dict[first_color]:
        dp[0][color] = 1001

    for i in range(1, N):
        for color, other_colors in other_color_dict.items():
            dp[i][color] = min(dp[i-1][other_colors[0]], dp[i-1][other_colors[1]]) + rgb_list[i][color]

    for color in other_color_dict[first_color]:
        if min_result > dp[-1][color]:
            min_result = dp[-1][color]

print(min_result)
