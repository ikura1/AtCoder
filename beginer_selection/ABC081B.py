import sys

input = sys.stdin.readline


def main():
    n = int(input())
    a_list = [int(i) for i in input().split()]
    print(min([len(bin(i).split("1")[-1]) for i in a_list]))


if __name__ == "__main__":
    main()
