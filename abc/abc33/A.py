import sys

input = sys.stdin.readline


def main():
    print("SAME" if len(set(input().strip())) == 1 else "DIFFERENT")


if __name__ == "__main__":
    main()
