import sys

input = sys.stdin.readline


def main():
    print("\n".join([input().strip()[::-1] for _ in range(4)][::-1]))


if __name__ == "__main__":
    main()
