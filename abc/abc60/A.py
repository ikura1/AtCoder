import sys

input = sys.stdin.readline


def main():
    a, b, c = input().split()
    print("YES" if a[-1] == b[0] and b[-1] == c[0] else "NO")


if __name__ == "__main__":
    main()
