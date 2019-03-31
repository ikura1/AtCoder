import sys

input = sys.stdin.readline


def main():
    # たしかに、rangeで回したらいいよね
    a, b, c, x = [int(input()) for _ in range(4)]
    # 50単位だから50で割るの頭いい
    x //= 50
    ans = 0
    for i in range(a + 1):
        if 10 * i > x:
            break
        rem = x - 10 * i
        for j in range(b + 1):
            if 2 * j > rem:
                break
            # 50と100は丁度か50で埋めれるから、+1か
            if rem - 2 * j <= c:
                ans += 1


if __name__ == "__main__":
    main()
