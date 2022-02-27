# 연월일 달력

def date_check(date):
    year, month, day = map(int, (date[0:4], date[4:6], date[6:]))
    if month > 12 or month == 0:
        return -1
    else:
        if month == 2 and 0 < day < 29:
            pass
        elif month in [1, 3, 5, 7, 8, 10, 12] and 0 < day < 32:
            pass
        elif month in [4, 6, 9, 11] and 0 < day < 31:
            pass
        else:
            return -1
        return '{:04.0f}/{:02.0f}/{:02.0f}'.format(year, month, day)


n = int(input())
for i in range(n):
    date = input()
    result = date_check(date)
    print(f'#{i + 1} {result}')
