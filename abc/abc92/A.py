import sys

input = sys.stdin.readline


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print((a if a < b else b) + (c if c < d else d))


if __name__ == "__main__":
    main()
