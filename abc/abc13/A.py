import sys

input = sys.stdin.readline


def main():
    print(["A", "B", "C", "D", "E"].index(input().strip()) + 1)


if __name__ == "__main__":
    main()
