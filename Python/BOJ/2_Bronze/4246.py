# To and Fro

while True:
    N = int(input())
    if not N:
        break
    txt = input()
    temp = []
    for i in range(0, len(txt), N):
        temp.append(txt[i+N-1:i-1:-1] if i//N % 2 else txt[i:i+N])
    print(''.join(map(lambda x: ''.join(x), list(zip(*temp)))))
