def mult(num: str) -> int:
    result = 1
    for n in num:
        result *= int(n)
    return result


num = input()

for i in range(1, len(num)):
    if mult(num[:i]) == mult(num[i:]):
        print("YES")
        break

else:
    print("NO")
