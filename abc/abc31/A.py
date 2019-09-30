import sys

input = sys.stdin.readline


def main():
    a, d = map(int, input().split())
    print(max((a + 1) * d, a * (d + 1)))


if __name__ == "__main__":
    main()
