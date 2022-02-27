N = int(input())
F = int(input())
num = (N//100)*100

for i in range(100):
    if (num+i)%F == 0:
        result = i
        break

print(f'{result:02.0f}')