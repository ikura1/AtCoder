import sys

input = sys.stdin.readline


def main():
    a, b = [int(i) for i in input().split()]
    print("Odd" if (a * b) % 2 else "Even")


if __name__ == "__main__":
    main()
