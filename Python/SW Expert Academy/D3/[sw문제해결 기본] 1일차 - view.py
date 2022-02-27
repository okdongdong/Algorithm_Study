def MyMax(nums):  # 리스트에서 최대값을 찾는 MyMax함수 정의
    try:
        max_num = nums[0]
        for num in nums:
            if num > max_num:
                max_num = num
        return max_num

    except:
        return None  # 리스트가 빈리스트일 경우 None 반환


# 문제풀이 시작
for tc in range(10):
    N = int(input())
    buildings = [int(i) for i in input().split()]
    result = 0

    for i in range(2, N - 2):  # 빌딩을 순회하며 조망권 판단

        area = buildings[i - 2:i + 3]  # 현재 빌딩과 좌우 2개의 빌딩에 대하여 구역 설정
        first_building = MyMax(area)

        if MyMax(area) == buildings[i]:
            second_building = MyMax(buildings[i - 2:i] + buildings[i + 1:i + 3])
            # 현재 빌딩이 가장 높은 건물일 경우 좌우에서 두번째로 높은 건물의 높이를 구함
            # => 현재 빌딩을 제외한 좌 우 4개의 건물 중 최대값 산정

            result += first_building - second_building
            # 가장높은 건물의 높이 - 두번째로 높은 건물의 높이 = 조망권이 확보된 세대 수

    print('#{} {}'.format(tc + 1, result))  # 테스트케이스 별 결과 출력
