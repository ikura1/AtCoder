import sys

input = sys.stdin.readline


def main():
    a, b, c = map(int, input().split())
    print(a * b * 2 + a * c * 2 + b * c * 2)


if __name__ == "__main__":
    main()
