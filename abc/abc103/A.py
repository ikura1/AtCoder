import sys

input = sys.stdin.readline


def main():
    a = sorted(map(int, input().split()))
    print(sum(a[1:]) - sum(a[:2]))


if __name__ == "__main__":
    main()
