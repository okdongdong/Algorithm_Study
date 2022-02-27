# 소금 폭탄
h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

h = h2-h1
m = m2-m1
s = s2-s1
m += s//60
s %= 60
h += m//60
m %= 60
h %= 24

result = f'{h:02.0f}:{m:02.0f}:{s:02.0f}'

print(result if result != '00:00:00' else '24:00:00')
