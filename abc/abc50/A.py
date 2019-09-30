import sys

input = sys.stdin.readline


def main():
    a, o, b = input().split()
    a = int(a)
    b = int(b)
    if o == "+":
        print(a + b)
    else:
        print(a - b)


if __name__ == "__main__":
    main()
