import sys

input = sys.stdin.readline


def main():
    N, L = [int(i) for i in input().split()]
    aji = [L + i for i in range(N)]
    print(sum(aji) - min(aji, key=abs))


if __name__ == "__main__":
    main()
