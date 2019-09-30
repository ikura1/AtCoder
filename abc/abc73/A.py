import sys

input = sys.stdin.readline


def main():
    n = input()
    print("Yes" if "9" in n else "No")


if __name__ == "__main__":
    main()
