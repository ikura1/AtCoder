import sys

input = sys.stdin.readline


def main():
    n = int(input())
    if n < 1000:
        print("ABC")
    else:
        print("ABD")


if __name__ == "__main__":
    main()
