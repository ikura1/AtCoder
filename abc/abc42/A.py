import sys

input = sys.stdin.readline


def main():
    print("YES" if sorted(map(int, input().split())) == [5, 5, 7] else "NO")


if __name__ == "__main__":
    main()
