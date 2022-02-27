def solution(record):
    #   ## 풀이1
    #     result = []
    #     my_record = list(map(lambda x:x.split(), record))
    #     user_name_dict = dict()

    #     for i in range(len(my_record)):
    #         cmd = my_record[i][0]
    #         if cmd == 'Enter' or cmd == 'Change':
    #             user_id, user_name = my_record[i][1:]
    #             user_name_dict[user_id] = user_name

    #     for i in range(len(my_record)):
    #         cmd, user_id = my_record[i][:2]
    #         if cmd == 'Enter':
    #             result.append(f'{user_name_dict[user_id]}님이 들어왔습니다.')
    #         elif cmd == 'Leave':
    #             result.append(f'{user_name_dict[user_id]}님이 나갔습니다.')

    #     ## 풀이2
    #     result = []
    #     my_record = []
    #     list(map(lambda x: my_record.extend(x.split()), record))
    #     user_name_dict = dict()
    #     i = 0
    #     while i < len(my_record):
    #         cmd = my_record[i]
    #         if cmd == 'Enter' or cmd == 'Change':
    #             user_id, user_name = my_record[i+1], my_record[i+2]
    #             user_name_dict[user_id] = user_name
    #             i += 3
    #         else:
    #             i += 2

    #     i = 0
    #     while i < len(my_record):
    #         cmd, user_id = my_record[i], my_record[i+1]
    #         if cmd == 'Enter':
    #             result.append(f'{user_name_dict[user_id]}님이 들어왔습니다.')
    #             i += 3
    #         elif cmd == 'Leave':
    #             result.append(f'{user_name_dict[user_id]}님이 나갔습니다.')
    #             i += 2
    #         else:
    #             i += 3

    # 풀이3
    result = []
    my_record = []
    for x in record:
        my_record.extend(x.split())

    user_name_dict = dict()
    i = 0
    while i < len(my_record):
        cmd = my_record[i]
        if cmd == 'Enter' or cmd == 'Change':
            user_id, user_name = my_record[i+1], my_record[i+2]
            user_name_dict[user_id] = user_name
            i += 3
        else:
            i += 2

    i = 0
    while i < len(my_record):
        cmd, user_id = my_record[i], my_record[i+1]
        if cmd == 'Enter':
            result.append(f'{user_name_dict[user_id]}님이 들어왔습니다.')
            i += 3
        elif cmd == 'Leave':
            result.append(f'{user_name_dict[user_id]}님이 나갔습니다.')
            i += 2
        else:
            i += 3

    return result

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
                "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
