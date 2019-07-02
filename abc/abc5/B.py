import sys

input = sys.stdin.readline


def main():
    N = int(input())
    print(min([int(input()) for _ in range(N)]))


if __name__ == "__main__":
    main()
