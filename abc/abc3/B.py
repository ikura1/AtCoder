import sys

input = sys.stdin.readline


def main():
    S = input().strip()
    T = input().strip()
    for i, j in zip(S, T):
        if i == j:
            continue
        elif (i in list("atcoder") and j == "@") or (j in list("atcoder") and i == "@"):
            continue
        else:
            print("You will lose")
            return
    print("You can win")


if __name__ == "__main__":
    main()
