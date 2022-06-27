# 24
now_hours, now_minutes, now_seconds = map(int, input().split(':'))
start_hours, start_minutes, start_seconds = map(int, input().split(':'))

now_times = now_hours*60*60 + now_minutes*60 + now_seconds
start_times = start_hours*60*60 + start_minutes*60 + start_seconds

result_times = start_times - now_times

result_times, result_seconds = divmod(result_times, 60)
result_times, result_minutes = divmod(result_times, 60)
result_hours = result_times % 24

print(f'{result_hours:02.0f}:{result_minutes:02.0f}:{result_seconds:02.0f}')
