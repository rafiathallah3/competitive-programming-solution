"""
Author: Rafi
Problem: Doremy's Paint 3
Link: https://codeforces.com/problemset/problem/1890/A
Created: 2026-08-02 12:34:09
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


def solve():
    n = ii()
    l = li()

    jumlah = Counter(l)
    if len(jumlah) > 2:
        print("No")
        return

    if len(jumlah) == 1:
        print("Yes")
        return

    s = list(set(l))
    bagiBawah = n // 2
    bagiAtas = (n + 1) // 2

    if (jumlah[s[0]] == bagiBawah and jumlah[s[1]] == bagiAtas) or (
        jumlah[s[0]] == bagiAtas and jumlah[s[1]] == bagiBawah
    ):
        print("Yes")
        return

    print("No")


def main():
    t = int(input())
    # t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()