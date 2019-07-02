import sys

input = sys.stdin.readline


def gcd(*args):
    a = max(args)
    b = min(args)
    while b != 0:
        a, b = b, a % b
    return a


def main():
    A, B, C, D = [int(i) for i in input().split()]
    # X : AとBの間の整数の数
    X = B - A + 1
    # Y : AとBの間でCの倍数の数
    Y = (B // C) - ((A - 1) // C)
    # Z : AとBの間でDの倍数の数
    Z = (B // D) - ((A - 1) // D)
    # V : CとDの最小公倍数
    V = (C * D) // gcd(C, D)
    # W : AとBの間でVの倍数の数
    W = (B // V) - ((A - 1) // V)
    print(X - Y - Z + W)


if __name__ == "__main__":
    main()
