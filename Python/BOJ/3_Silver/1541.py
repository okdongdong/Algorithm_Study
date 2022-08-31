nums = input().split('-')
result = sum(map(int, nums[0].split('+')))
result -= sum(map(lambda x: sum(map(int, x.split('+'))), nums[1:]))
print(result)
