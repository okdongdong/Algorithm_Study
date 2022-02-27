# 별 찍기 - 5
N = int(input())
for i in range(N):
    txt = '*'*(2*i +1)
    print(txt.rjust(N+i))