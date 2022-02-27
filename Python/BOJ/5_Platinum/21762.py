T = int(input())
for tc in range(T):
    X, Y, W = [], [], []
    X.extend(input())
    Y.extend(input())
    W.extend(input())
   
    # X에 대한 연산, 부분수열 원소 사이사이의 원소 도출
    ww = 0
    W_copy = W[:]
    X_com = []
    temp = []

    for i in range(len(X)-1,-1,-1):
        if W_copy and (not ww):
            ww = W_copy.pop()
        if ww == X[i]:
            X.pop(i)
            ww = 0
            X_com.append(temp)
            temp = []
        else:
            temp.append(X.pop())

    X_com.append(temp)

    # Y에 대한 연산
    ww = 0
    W_copy = W[:]
    Y_com = []
    temp = []
    for i in range(len(Y)-1,-1,-1):
        if W_copy and (not ww):
            ww = W_copy.pop()
        if ww == Y[i]:
            Y.pop(i)
            ww = 0
            Y_com.append(temp)
            temp = []
        else:
            temp.append(Y.pop())
    
    Y_com.append(temp)

    flag = False

    for i in range(len(X_com)):
        for c in X_com[i]:
            if c in Y_com[i]:
                flag = True
                break

        if flag:
            print(1)
            break
    else:
        print(0)