# 사다리 조작
import sys
input = sys.stdin.readline


def num_to_num_check():     # 사다리 출발 숫자와 도착 숫자가 일치하는지 확인
    for num in range(1, N):
        temp = num
        for h in range(1, H+1):
            if ladder[h][temp]:
                temp = ladder[h][temp]
        if temp != num:
            return False
    return True


def ladder_control():       # 재귀로 하니까 오류남
    result = 999
    if num_to_num_check():
        return 0

    for i in range(len(ladder_sequence)):
        h1, num11, num12 = ladder_sequence[i]
        if ladder[h1][num11] or ladder[h1][num12]:
            continue
        ladder[h1][num11] = num12
        ladder[h1][num12] = num11
        if num_to_num_check():
            return 1
            
        if result > 2:
            for j in range(i+1, len(ladder_sequence)):
                h2, num21, num22 = ladder_sequence[j]
                if ladder[h2][num21] or ladder[h2][num22]:
                    continue
                ladder[h2][num21] = num22
                ladder[h2][num22] = num21
                if num_to_num_check():
                    result = 2

                if result > 3:
                    for k in range(j+1, len(ladder_sequence)):
                        h3, num31, num32 = ladder_sequence[k]
                        if ladder[h3][num31] or ladder[h3][num32]:
                            continue
                        ladder[h3][num31] = num32
                        ladder[h3][num32] = num31
                        if num_to_num_check():
                            result= 3

                        ladder[h3][num31] = 0
                        ladder[h3][num32] = 0

                ladder[h2][num21] = 0
                ladder[h2][num22] = 0

        ladder[h1][num11] = 0
        ladder[h1][num12] = 0

    if result > 3:
        return -1
    return result


N, M, H = map(int, input().split())
ladder = [[0]*(N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a][b] = b+1
    ladder[a][b+1] = b
# 빈 칸의 좌표를 저장
ladder_sequence = []
for num in range(1, N):
    for h in range(1, H+1):
        if ladder[h][num] == 0 and ladder[h][num+1] == 0:
            ladder_sequence.append((h, num, num+1))

result = ladder_control()
print(result)