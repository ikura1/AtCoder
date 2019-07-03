import sys

input = sys.stdin.readline


def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    print(max([i for i in a if i < max(a)]))


if __name__ == "__main__":
    main()
