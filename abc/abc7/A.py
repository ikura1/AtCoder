import sys

input = sys.stdin.readline


def main():
    n = int(input())
    print(n - 1 if n else 0)


if __name__ == "__main__":
    main()
