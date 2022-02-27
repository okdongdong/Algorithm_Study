# 랜선 자르기

K, N = map(int, input().split())
lan_cables = [int(input()) for _ in range(K)]
left = 0
right = max(lan_cables)
result = []
cnt = 0
while cnt < 40:
    cable_cnt = 0
    mid = (left + right)//2
    if mid == 0:
        mid +=1
    for cable in lan_cables:
        cable_cnt += cable//mid
    
    if cable_cnt <N:
        right = mid

    elif cable_cnt>=N:
        result.append(mid)
        left = mid +1

    cnt += 1

print(max(result))