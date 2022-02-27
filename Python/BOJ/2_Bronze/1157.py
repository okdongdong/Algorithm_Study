S = input()
S = S.upper()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lst = [0]*26

for i in S:
    lst[alpha.index(i)] += 1

fa=lst.index(max(lst))
lst.sort(reverse = True)

if lst[0]==lst[1]:
    print("?")
else:
    print(alpha[fa])

