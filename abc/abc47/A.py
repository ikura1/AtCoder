import sys

input = sys.stdin.readline


def main():
    a, b, c = sorted(map(int, input().split()))
    print("Yes" if a + b == c else "No")


if __name__ == "__main__":
    main()
