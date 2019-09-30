import sys

input = sys.stdin.readline


def main():
    kane = 700
    a, b, c = input().strip()
    if a == "o":
        kane += 100
    if b == "o":
        kane += 100
    if c == "o":
        kane += 100
    print(kane)


if __name__ == "__main__":
    main()
