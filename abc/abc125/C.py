import sys
import fractions as math
from functools import reduce

input = sys.stdin.readline


def gcd(nums):
    return reduce(math.gcd, nums)


def gcd2(index, a_list):
    nums = a_list[:]
    del nums[index]
    return gcd(nums)


def main():
    n = int(input())
    a_list = [int(i) for i in input().split()]
    if n > 10:
        n = 10
    # 妨げになる値の発見方法
    # 最小公倍数の方がいいのか？？
    #
    print(max([gcd2(i, a_list) for i in range(n)]))


if __name__ == "__main__":
    main()
