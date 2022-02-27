S = input()
lst=[-1]*26
alpha='abcdefghijklmnopqrstuvwxyz'
for txt in S:
     if lst[alpha.index(txt)] == -1:
         lst[alpha.index(txt)] = S.index(txt)
print(*lst)