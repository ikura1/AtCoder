import sys

input = sys.stdin.readline


def main():
    a = int(input())
    b = int(input())
    n = int(input())
    for i in range(n, 10 ** 5):
        if i % a == 0 and i % b == 0:
            print(i)
            break


if __name__ == "__main__":
    main()
