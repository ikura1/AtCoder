import sys

input = sys.stdin.readline


def main():
    test = [[int(i) for i in input().split()] for _ in range(3)]
    print(int(sum(map(lambda x: x[0] * x[1] * 0.1, test))))


if __name__ == "__main__":
    main()
