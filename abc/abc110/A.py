import sys

input = sys.stdin.readline


def main():
    a, b, c = sorted(input().split(), reverse=True)
    print(int(a + b) + int(c))


if __name__ == "__main__":
    main()
