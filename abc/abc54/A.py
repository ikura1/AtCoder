import sys

input = sys.stdin.readline


def main():
    a, b = map(int, input().split())
    if a == b:
        print("Draw")
    elif a == 1 or (b < a and b != 1):
        print("Alice")
    else:
        print("Bob")


if __name__ == "__main__":
    main()
