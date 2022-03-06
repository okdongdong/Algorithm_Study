# 햄버거 사랑
n, m, t = map(int, input().split())
buger = [0, t]
for i in range((t//n)+1):
    j = (t-i*n)//m

    buger = sorted((buger, [i+j, t-i*n-j*m]), key=lambda x: (x[1], -x[0]))[0]

print(*buger)
