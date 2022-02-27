n = int(input())

for i in range(n):
    N, K = map(int, input().split())
    length = int(N/4)
    num0 = input()
    txt = ''

    for j in range(length):
        num0 = num0[-1]+num0[:-1]
        txt += num0

    set0 = set(map(''.join, zip(*[iter(txt)]*length)))
    lst0 = sorted(list(set0), reverse=True)
    result = int(lst0[K-1], 16)

    print(f"#{i+1} {result}")


# 16진수인 비밀번호를 찾는 문제였음

# 비밀번호의 길이가 문자열 길이에 따라 달라지는 것을 모르고 3글자 고정인 것으로 풀다가 시간이 오래 걸림

