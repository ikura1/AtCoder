import sys

input = sys.stdin.readline


def main():
    n, x = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    print(sum([a[i] for i, f in enumerate("{:b}".format(x)[::-1]) if f == "1"]))


if __name__ == "__main__":
    main()
