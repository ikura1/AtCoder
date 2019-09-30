import sys

input = sys.stdin.readline


def main():
    m, d = [int(i) for i in input().split()]
    print("YES" if m % d == 0 else "NO")


if __name__ == "__main__":
    main()
