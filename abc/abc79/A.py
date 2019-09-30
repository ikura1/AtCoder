import sys

input = sys.stdin.readline


def main():
    n = input().strip()
    print("Yes" if len(set(n[1:])) == 1 or len(set(n[:-1])) == 1 else "No")


if __name__ == "__main__":
    main()
