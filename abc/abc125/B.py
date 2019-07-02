import sys

input = sys.stdin.readline


def main():
    n = input()
    obj = [int(i) for i in input().split()]
    costs = [int(i) for i in input().split()]
    print(sum(filter([o - c for o, c in zip(obj, costs)], lambda x: x > 0)))


if __name__ == "__main__":
    main()
