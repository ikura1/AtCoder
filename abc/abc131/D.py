import itertools
import sys

input = sys.stdin.readline


def main():
    # クリティカルパルかなんか？
    # 累積和つかう？
    # 仕事が期限までに終わらせるかどうか
    # ナーススケジューリング問題？
    # 締切とタスクの合計値
    # 累積和となんかやと思うんやがな…
    # うーん、答えがわからん
    N = int(input())
    task_list = sorted(
        [[int(i) for i in input().split()] for _ in range(N)], key=lambda x: x[1]
    )
    print(
        "Yes"
        if all(
            [
                j <= i[1]
                for i, j in zip(
                    task_list, itertools.accumulate(map(lambda x: x[0], task_list))
                )
            ]
        )
        else "No"
    )


if __name__ == "__main__":
    main()
