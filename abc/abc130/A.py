import sys

input = sys.stdin.readline


def main():
    x, a = [int(i) for i in input().split()]
    res = 0 if a > x else 10
    print(res)


if __name__ == "__main__":
    main()
