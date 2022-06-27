# 쇠막대기
pipes = input()
stack = []
result = 0
for i in range(len(pipes)):
    pipe = pipes[i]
    if pipe == '(':
        stack.append(1)

    elif pipes[i-1] == '(' and pipe == ')':
        stack.pop()
        result += len(stack)

    else:
        stack.pop()
        result += 1

print(result)
