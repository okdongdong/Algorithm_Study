txt=input()

lst=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in lst:
    txt = txt.replace(i,'0')

print(len(txt))