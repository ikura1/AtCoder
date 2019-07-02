import sys

input = sys.stdin.readline


def main():
    print("".join([i for i in input().strip() if i not in ("a", "i", "u", "e", "o")]))


if __name__ == "__main__":
    main()
