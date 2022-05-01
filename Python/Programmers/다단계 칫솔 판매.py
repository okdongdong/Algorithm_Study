def solution(enroll, referral, seller, amount):

    # 윗사람과 연결관계 기록
    network_dict = {}
    for idx, name in enumerate(enroll):
        network_dict[name] = referral[idx]

    revenue_dict = {}

    # 윗사람한테 수익 배분 함수
    def revenue_share(revenue, name):
        if name == '-' or revenue == 0:
            return

        next_revenue = int(revenue * .1)
        next_name = network_dict[name]

        if revenue_dict.get(name):
            revenue_dict[name] += revenue - next_revenue
        else:
            revenue_dict[name] = revenue - next_revenue

        revenue_share(next_revenue, next_name)

    # 수익배분
    for idx, name in enumerate(seller):
        revenue = amount[idx]*100
        revenue_share(revenue, name)

    # 결과기록
    answer = []
    for name in enroll:
        if revenue_dict.get(name):
            answer.append(revenue_dict[name])
        else:
            answer.append(0)

    return answer


print(solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["young", "john", "tod", "emily", "mary"],
    [12, 4, 2, 5, 10]
))
