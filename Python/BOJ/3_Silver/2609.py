a, b = map(int, input().split())
num1 = min(a, b)

for num in range(1, num1+1):
    if not a%num and not b%num:
        GCF = num

LCM = (a*b) // GCF

print(GCF, LCM, sep='\n')