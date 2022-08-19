import sys
input = sys.stdin.readline


def player_in_field(player_x, player_y):
    if X <= player_x <= X+W and Y <= player_y <= Y+H:
        return 1

    if (X - player_x)**2 + (Y+H/2 - player_y)**2 <= (H/2)**2:
        return 1

    if (X+W - player_x)**2 + (Y+H/2 - player_y)**2 <= (H/2)**2:
        return 1

    return 0


W, H, X, Y, P = map(int, input().split())
cnt = 0
for _ in range(P):
    player_x, player_y = map(int, input().split())
    cnt += player_in_field(player_x, player_y)

print(cnt)
