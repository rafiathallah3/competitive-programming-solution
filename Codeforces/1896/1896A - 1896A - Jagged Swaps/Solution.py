"""
Author: Rafi
Problem: Jagged Swaps
Link: https://codeforces.com/problemset/problem/1896/A
Created: 2026-08-01 19:37:13
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
    a = li()

    print("YES" if a[0] == 1 else "NO")


def main():
    t = int(input())
    # t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()