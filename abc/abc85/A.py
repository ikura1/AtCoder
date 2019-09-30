import sys

input = sys.stdin.readline


def main():
    print("/".join(["2018" if i == "2017" else i for i in input().split("/")]))


if __name__ == "__main__":
    main()
