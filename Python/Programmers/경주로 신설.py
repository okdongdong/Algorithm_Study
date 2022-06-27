from heapq import heappush, heappop


def solution(board):
    drc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    R, C = len(board), len(board[0])

    # (cost, position, direction)
    heap = [(0, (0, 0), (0, 1)), (0, (0, 0), (1, 0))]
    cost_board = [[[987654321]*4 for _ in range(C)] for _ in range(R)]

    while heap:
        cost, position, direction = heappop(heap)

        r, c = position

        for (dr, dc), idx in enumerate(drc):
            if direction == (-dr, -dc):
                continue

            nr, nc = r+dr, c+dc

            if not (0 <= nr < R and 0 <= nc < C) or board[nr][nc]:
                continue

            if (dr, dc) == direction:
                if cost_board[nr][nc][idx] < cost+100:
                    heap_item = (cost+100, (nr, nc), (dr, dc))

            else:
                if cost_board[nr][nc][idx] < cost+600:
                    heap_item = (cost+600, (nr, nc), (dr, dc))  # 100+500

            heappush(heap, heap_item)

    return min(cost_board[-1][-1])
