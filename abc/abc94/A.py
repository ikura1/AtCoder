import sys

input = sys.stdin.readline


def main():
    a, b, x = map(int, input().split())
    print("YES" if x <= a + b and x >= a else "NO")


if __name__ == "__main__":
    main()
