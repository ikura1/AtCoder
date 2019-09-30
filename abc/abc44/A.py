import sys

input = sys.stdin.readline


def main():
    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    if k >= n:
        print(n * x)
    else:
        print(k * x + (n - k) * y)


if __name__ == "__main__":
    main()
