import sys

input = sys.stdin.readline


def main():
    x, y = [int(i) for i in input().split()]
    print(y // x)


if __name__ == "__main__":
    main()
