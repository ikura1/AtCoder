import sys
from itertools import combinations


def main():
    input = sys.stdin.readline
    antena_list = [int(input()) for _ in range(5)]
    k = int(input())
    max_length = max([j - i for i, j in combinations(antena_list, 2)])
    print(":(" if max_length > k else "Yay!")


if __name__ == "__main__":
    main()
