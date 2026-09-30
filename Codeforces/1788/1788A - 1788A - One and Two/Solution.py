"""
Author: Rafi
Problem: One and Two
Link: https://codeforces.com/problemset/problem/1788/A
Created: 2026-08-11 23:37:18
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

    berapa2 = l.count(2)

    if (berapa2 % 2) & 1:
        print(-1)
        return

    if berapa2 <= 0:
        print(1)
        return

    jumlah2Perlu = berapa2 // 2
    hasil = 0

    for i in range(n):
        if l[i] == 2:
            hasil += 1
        if jumlah2Perlu == hasil:
            print(i + 1)
            return


def main():
    t = int(input())
    # t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()