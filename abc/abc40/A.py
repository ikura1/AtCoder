import sys

input = sys.stdin.readline


def main():
    n, x = map(int, input().split())
    print(min(x - 1, n - x))


if __name__ == "__main__":
    main()
