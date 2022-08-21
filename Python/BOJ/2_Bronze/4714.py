import sys
input = sys.stdin.readline

while True:
    X = float(input())
    if X < 0:
        break

    print(
        f'Objects weighing {X:0.02f} on Earth will weigh {X*0.167:0.02f} on the moon.')
