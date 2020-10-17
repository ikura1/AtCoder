import sys

input = sys.stdin.readline


def get(min_value, block):
    while True:
        min_value += 1
        if min_value not in block:
            return min_value


def main():
    n = int(input())
    p = map(int, input().split())
    min_value = 0
    block = set()
    for i in p:
        block.add(i)
        if i == min_value:
            min_value = get(min_value, block)
        print(min_value)


if __name__ == "__main__":
    main()
