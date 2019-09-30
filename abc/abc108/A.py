import sys

input = sys.stdin.readline


def main():
    k = int(input())
    print(k // 2 * (k - (k // 2)))


if __name__ == "__main__":
    main()
