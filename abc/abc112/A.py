import sys

input = sys.stdin.readline


def main():
    n = input().strip()
    if n == "1":
        print("Hello World")
    else:
        print(int(input()) + int(input()))


if __name__ == "__main__":
    main()
