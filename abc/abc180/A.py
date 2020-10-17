import sys

input = sys.stdin.readline


def main():
    n, a, b = map(int, input().split())
    print(n - a + b)


if __name__ == "__main__":
    main()
