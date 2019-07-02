import sys

input = sys.stdin.readline


def main():
    a, b = [int(i) for i in input().split()]
    if a == b:
        print(a + b)
    else:
        max_ = max([a, b])
        print(max_ * 2 - 1)


if __name__ == "__main__":
    main()
