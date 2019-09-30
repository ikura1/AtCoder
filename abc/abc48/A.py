import sys

input = sys.stdin.readline


def main():
    print("".join([i[0] for i in input().split()]))


if __name__ == "__main__":
    main()
