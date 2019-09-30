import sys

input = sys.stdin.readline


def main():
    n = input().strip()
    print("Yes" if n == n[::-1] else "No")


if __name__ == "__main__":
    main()
