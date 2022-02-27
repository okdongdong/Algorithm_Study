def sudoku(idx):
    if idx == len(target_rc_list):
        return True

    r, c = target_rc_list[idx]
    for i in range(1, 10):
        if i in r_nums[r] or i in c_nums[c] or i in square_nums[r//3][c//3]:
            continue
        
        arr[r][c] = i
        r_nums[r].add(i)
        c_nums[c].add(i)
        square_nums[r//3][c//3].add(i)
       
        if sudoku(idx + 1):
            break
       
        arr[r][c] = 0
        r_nums[r].remove(i)
        c_nums[c].remove(i)
        square_nums[r//3][c//3].remove(i)
    
    else:
        return False
    
    return True


arr = [list(map(int, list(input()))) for _ in range(9)]
r_nums = [set() for _ in range(9)]
c_nums = [set() for _ in range(9)]
square_nums = [[set() for _ in range(3)] for _ in range(3)]
target_rc_list = []
for r in range(9):
    for c in range(9):
        if arr[r][c]:
            r_nums[r].add(arr[r][c])
            c_nums[c].add(arr[r][c])
            square_nums[r//3][c//3].add(arr[r][c])
        else:
            target_rc_list.append((r, c))

sudoku(0)

for r in range(9):
    print(*arr[r],sep='')
