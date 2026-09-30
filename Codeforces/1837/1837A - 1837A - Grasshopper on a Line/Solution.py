"""
Author: Rafi
Problem: Grasshopper on a Line
Link: https://codeforces.com/problemset/problem/1837/A
Created: 2026-08-09 22:35:53
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
    n, k = mi()

    if n < k:
        print(1)
        print(n)
        return

    if n % k == 0:
        print(2)
        print(n - 1, 1)
        return

    print(1)
    print(n)


def main():
    t = int(input())
    # t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()