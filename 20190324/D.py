import sys
from itertools import product


def ignore(txt, ignore_list):
    for i in ignore_list:
        if i in txt:
            return True
    return False


def main():
    input = sys.stdin.readline
    # n = int(input())
    n = 4
    chars = ("A", "C", "G", "T")
    pro = ["".join(i) for i in list(product(chars, repeat=n))]
    ignore_master = "AGC"
    print(len(pro))
    print(len([i for i in pro if not ignore(i, ["AGC", "GAC", "ACG"])]))


if __name__ == "__main__":
    main()
