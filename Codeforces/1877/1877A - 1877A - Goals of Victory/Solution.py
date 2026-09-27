"""
Author: Rafi
Problem: Goals of Victory
Link: https://codeforces.com/problemset/problem/1877/A
Created: 2026-08-10 22:02:29
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

    print(sum(l) * -1)


def main():
    t = int(input())
    # t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()