from itertools import permutations
import heapq


def solution(board, r, c):
    drc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    min_cnt = 999
    cards = set([])

    for i in range(4):
        for j in range(4):
            if board[i][j]:
                cards.add(board[i][j])

    # 카드를 고르는 최대 경우의 수 6! = 720 가지
    cards_order_list = list(permutations(cards, len(cards)))

    def move(_r, _c, card, _cnt=0):
        que = [(_cnt, _r, _c)]

        if not visited[_r][_c] and board[_r][_c] == card:
            visited[_r][_c] = True
            return _r, _c, 0

        while que:
            cnt, r, c = heapq.heappop(que)

            for dr, dc in drc:
                for i in range(1, 4):
                    nr, nc = r + dr*i, c+dc*i
                    if not (0 <= nr < 4 and 0 <= nc < 4):
                        break

                    if board[nr][nc] == card:
                        visited[nr][nc] = True
                        return nr, nc, cnt+1

                    if not (0 <= nr+dr < 4 and 0 <= nc+dc < 4):
                        heapq.heappush(que, (cnt+1, nr, nc))
                        break

                    if (not visited[nr][nc] and board[nr][nc] and board[nr][nc] != card):
                        heapq.heappush(que, (cnt+1, nr, nc))
                        break

                    if i == 1:
                        heapq.heappush(que, (cnt+1, nr, nc))

    for cards_order in cards_order_list:
        visited = [[False]*4 for _ in range(4)]

        cnt = 0
        nr, nc = r, c
        for card in cards_order:
            if cnt >= min_cnt:
                break

            nr, nc, now_cnt = move(nr, nc, card)
            cnt += now_cnt
            nr, nc, now_cnt = move(nr, nc, card)
            cnt += now_cnt

        else:
            min_cnt = min(min_cnt, cnt)

    return min_cnt + len(cards)*2


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
