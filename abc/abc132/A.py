import sys

input = sys.stdin.readline


def main():
    print("Yes" if len(set(input().strip())) == 2 else "No")


if __name__ == "__main__":
    main()
