import sys


def main():
    input = sys.stdin.readline
    n = int(input())
    nin_list = [int(input()) for _ in range(5)]
    num_list = [n / i + 1 if n % i else n / i for i in nin_list]
    print(4 + max(num_list))


if __name__ == "__main__":
    main()
