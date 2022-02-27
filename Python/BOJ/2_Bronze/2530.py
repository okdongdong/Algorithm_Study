# 인공지능 시계

h, m, s = map(int, input().split())
temp = int(input())

temp, s = divmod(s+temp, 60)
temp, m = divmod(m+temp, 60)
temp, h = divmod(h+temp, 24)

print(h, m, s)