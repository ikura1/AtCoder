import sys

input = sys.stdin.readline


def main():
    x, a, b = map(int, input().split())
    if b - a <= 0:
        print("delicious")
    elif b - a <= x:
        print("safe")
    else:
        print("dangerous")


if __name__ == "__main__":
    main()
