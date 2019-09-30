import sys

input = sys.stdin.readline


def main():
    s = input().strip()
    print("YES" if s[-1] == "T" else "NO")


if __name__ == "__main__":
    main()
