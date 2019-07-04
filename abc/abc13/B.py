import sys

input = sys.stdin.readline


def main():
    a = int(input())
    b = int(input())
    print(min([a - b if a >= b else b - a, 10 - max([a, b]) + min([a, b])]))


if __name__ == "__main__":
    main()
