"""
Author: Rafi
Problem: Desorting
Link: https://codeforces.com/problemset/problem/1853/A
Created: 2026-08-09 18:43:27
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

    for i in range(n - 1):
        if l[i + 1] < l[i]:
            print(0)
            return 0

    hasilList = []
    for i in range(n - 1):
        hasilList.append(((l[i + 1] - l[i]) // 2) + 1)

    print(min(hasilList))


def main():
    t = int(input())
    # t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()