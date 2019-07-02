import sys

input = sys.stdin.readline


def main():
    N = int(input())
    print("YES" if N % 3 == 0 else "NO")


if __name__ == "__main__":
    main()
