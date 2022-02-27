a,b = map(str, input().split())

for i in range(3):
    a = a[::-1] # 역순으로 배열
    print(a)
    b = b[::-1]

if int(a) > int(b):
    print(a)
else:
    print(b)