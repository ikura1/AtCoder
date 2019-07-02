import sys

input = sys.stdin.readline


def main():
    a, b, c = [int(i) for i in input().split()]
    min_ = min([a, b])
    max_ = max([a, b])
    print("Yes" if min_ <= c <= max_ else "No")


if __name__ == "__main__":
    main()
