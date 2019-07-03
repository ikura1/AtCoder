import sys

input = sys.stdin.readline


def main():
    n = int(input())
    s = [input().strip() for _ in range(n)]
    print(max(s, key=lambda x: s.count(x)))


if __name__ == "__main__":
    main()
