import sys

input = sys.stdin.readline


def main():
    s = input().strip()
    n = int(input())
    print([c1 + c2 for c1 in s for c2 in s][n - 1])


if __name__ == "__main__":
    main()
