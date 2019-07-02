import sys

input = sys.stdin.readline


def main():
    N = int(input())
    a = [0, 0, 1]
    if N <= 3:
        print(a[N - 1])
        return
    for i in range(3, N):
        # 割るのピンっとこない…
        # つらい…
        a[i % 3] = sum(a) % 10007
    print(a[i % 3])


if __name__ == "__main__":
    main()
