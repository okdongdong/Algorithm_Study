def Guitar(n, min_string, min_pack):

    cnt6, cnt = divmod(n, 6)

    if min_string * 6 <= min_pack:   # 낱개의 가격이 현저히 낮은 경우
        return n * min_string

    if min_pack < min_string * cnt:  # 묶음의 가격이 현저히 낮은 경우
        return (cnt6+1) * min_pack

    return (cnt * min_string) + (cnt6 * min_pack)


N, M = map(int, input().split())     # 패키지 기타 줄 수 : 6

min_result = 100001                  # 각 값 범위의 최대값보다 큰값으로 초기화
min_pack = 1001
min_string = 1001

for _ in range(M):
    pack, string = map(int, input().split())

    if min_pack > pack:              # 6개 패키지의 최솟값을 구함
        min_pack = pack

    if min_string > string:          # 낱개의 최솟값을 구함
        min_string = string

print(Guitar(N, min_string, min_pack))  # 함수를 통해 최솟값 산정
