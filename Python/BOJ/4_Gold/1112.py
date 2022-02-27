# 진법 변환
X, b = map(int, input().split())
result = ''
flag = X < 0 and b > 0
if flag:
    X = abs(X)

while X:
    X, temp = divmod(X, b)
    if temp < 0:
        X += 1
        temp -= b
    result += str(temp)

result += '-' if flag else ''

print(result[::-1] if result else 0)
