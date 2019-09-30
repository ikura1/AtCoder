import sys

input = sys.stdin.readline


def main():
    a, b, c, k = map(int, input().split())
    s, t = map(int, input().split())
    total = s * a + b * t
    if k <= s + t:
        total -= (s + t) * c
    print(total)


if __name__ == "__main__":
    main()
