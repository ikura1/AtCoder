import sys

input = sys.stdin.readline


def main():
    n, a, b = [int(i) for i in input().split()]
    print(min([a * n, b]))


if __name__ == "__main__":
    main()
