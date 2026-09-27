"""
Author: Rafi
Problem: Kefa and Park
Link: https://codeforces.com/problemset/problem/580/C
Created: 2026-08-09 23:00:57
"""

import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
from math import gcd, sqrt, ceil, floor, factorial

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().strip()


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


def cari(
    grafik: dict[int, list],
    posisi: int,
    keluarga: int,
    m: int,
    merah: list[int],
    berapaMerah: int,
) -> int:
    if merah[posisi - 1] == 0:
        berapaMerah = 0

    if berapaMerah > m:
        return 0

    anak = [i for i in grafik[posisi] if i != keluarga]
    if len(anak) <= 0:
        return 1

    hasil = 0
    for i in anak:
        hasil += cari(
            grafik,
            i,
            posisi,
            m,
            merah,
            berapaMerah + merah[i - 1] if merah[i - 1] == 1 else 0,
        )

    return hasil


def solve():
    n, m = mi()
    l = li()

    grafik: dict[int, list] = {}

    for i in range(n - 1):
        x, y = mi()
        grafik.setdefault(x, [])
        grafik.setdefault(y, [])
        grafik[x].append(y)
        grafik[y].append(x)

    print(cari(grafik, 1, 0, m, l, l[0]))


def main():
    # t = int(input())
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()