import sys

input = sys.stdin.readline


def main():
    n = int(input())
    print(":".join(map(lambda x: str(x).zfill(2), [n // 3600, n // 60 % 60, n % 60])))


if __name__ == "__main__":
    main()
