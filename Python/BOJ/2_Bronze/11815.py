N = int(input())
print(' '.join(map(lambda x: '1' if int(int(x)**.5)
      ** 2 == int(x) else '0', input().split())))
