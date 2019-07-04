import sys

input = sys.stdin.readline


def main():
    print(" ".join(input().split()[::-1]))


if __name__ == "__main__":
    main()
