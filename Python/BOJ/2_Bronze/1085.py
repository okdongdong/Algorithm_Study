x, y, w, h = map(int, input().split())

min_x = x if x < w-x else w-x
min_y = y if y < h-y else h-y

print(min_x if min_x < min_y else min_y)
