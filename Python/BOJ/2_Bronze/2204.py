# 도비의 난독증 테스트 다국어

while True:

    N = int(input())

    if N == 0:
        break

    word = input()
    for _ in range(N-1):
        new_word = input()
        if word.lower() > new_word.lower():
            word = new_word

    print(word)
