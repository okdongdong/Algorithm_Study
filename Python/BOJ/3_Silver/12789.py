N = int(input())

line = list(map(int, input().split()))[::-1]  # 1. pop()를 위해 뒤집어줌
line_stack = [1001]                           # 2. 인덱스 에러 방지

cnt = 1                     # 3. 현재 들어갈 수 있는 순서
while line:                 # 4. 모든 사람이 옮겨질때까지 반복

    if line[-1] == cnt:     # 5. 현재 입장가능한 번호가 대기열의 마지막 사람인경우
        line.pop()
        cnt += 1

    elif line_stack[-1] == cnt:     # 6. 현재 입장가능한 번호가 옆공간에 마지막으로 들어간 사람인 경우
        line_stack.pop()
        cnt += 1

    else:                           # 7. 입장이 불가능한 경우
        temp = line.pop()
        if line_stack[-1] > temp:
            line_stack.append(temp)

        else:                       # 8. 옆 공간에 들어간 사람보다 번호가 높은 사람이 들어갈 경우 이동불가
            result = 'Sad'
            break

else:                               # 9. 모든사람이 들어가는 경우 이동가능
    result = 'Nice'

print(result)
