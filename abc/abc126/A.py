import sys

input = sys.stdin.readline


def main():
    n, k = [int(i) for i in input().strip().split()]
    s = input().strip()
    print("".join([c.lower() if i == k else c for i, c in enumerate(s, start=1)]))


if __name__ == "__main__":
    main()
