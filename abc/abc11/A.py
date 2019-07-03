import sys

input = sys.stdin.readline


def main():
    n = int(input())
    print(1 if n == 12 else n + 1)


if __name__ == "__main__":
    main()
