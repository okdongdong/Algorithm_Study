# 핸드폰 요금

N = int(input())
call_times = list(map(int, input().split()))

y, m = 0, 0

for call_time in call_times:
    y += (call_time//30 + 1)*10
    m += (call_time//60 + 1)*15

if y == m:
    print(f'Y M {y}')
elif y > m:
    print(f'M {m}')
else:
    print(f'Y {y}')
