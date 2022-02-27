# TV 크기

a, b, c = map(int, input().split())
x = (a**2 / (b**2 + c**2))**0.5
print(int(b*x), int(c*x))