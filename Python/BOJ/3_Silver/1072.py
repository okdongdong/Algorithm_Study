# 게임

def game(left, right):
    if right - left < 2:
        return left

    mid = (left + right)//2
    new_num = int(100 * (Y + mid)/(X + mid))

    if old_num >= 99:   # 99이상일 경우 아무리 더해도 99를 넘을 수 없음
        return -1

    if new_num > old_num:
        return game(left, mid)
    else:
        return game(mid, right)


X, Y = map(int, input().split())

old_num = int(100 * Y / X)
a = game(0, 2*X)    # 그냥 x로 할경우 97%에서 걸림

while a >= 0:
    new_num = int(100 * (Y + a)/(X + a))

    if new_num > old_num:
        break

    a += 1

print(a)
