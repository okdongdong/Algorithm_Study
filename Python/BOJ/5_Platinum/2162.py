# 선분 그룹

# CCW를 이용한 선분교차 판별
# Counter Clock Wise
# 삼각형의 면적을 구하는 공식 + 벡터를 사용하여 S 값을 구함

#          | x1 y1 1 |
# 2 * S == | x2 y2 1 | == (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)
#          | x3 y3 1 |

# S > 0 : 반시계 방향
# S == 0 : 세 점이 평행
# S < 0 :시계 방향

import sys
input = sys.stdin.readline


def find_head(num):
    if num == head[num]:
        return num

    head[num] = find_head(head[num])
    return head[num]


def union(num1, num2):
    head1 = find_head(num1)
    head2 = find_head(num2)

    if head1 != head2:
        head[head2] = head1


def ccw(a, b, c):
    return (b[0] - a[0])*(c[1] - a[1]) - (b[1]-a[1])*(c[0]-a[0])


N = int(input())
head = list(range(N))

points_list = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if (x1, y1) > (x2, y2):
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    points_list.append(((x1, y1), (x2, y2)))

for i in range(N-1):
    for j in range(i+1, N):
        a, b = points_list[i]
        c, d = points_list[j]
        abc = ccw(a, b, c)
        abd = ccw(a, b, d)
        cda = ccw(c, d, a)
        cdb = ccw(c, d, b)

        if abc * abd <= 0 and cda * cdb <= 0:
            if abc * abd == 0 and cda * cdb == 0:
                if a <= d and b >= c:
                    union(i, j)

            else:
                union(i, j)

num_cnt = [0]*N
for num in head:
    num_cnt[find_head(num)] += 1

cnt = 0
for num in num_cnt:
    if num > 0:
        cnt += 1

print(cnt)
print(max(num_cnt))
