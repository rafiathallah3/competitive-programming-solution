"""
Author: Rafi
Problem: Maximum Increase
Link: https://codeforces.com/problemset/problem/702/A
Created: 2026-08-22 23:55:56
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

    palingPanjang = 1
    berapa = 1
    for i in range(1, n):
        if l[i] > l[i - 1]:
            berapa += 1
        else:
            berapa = 1

        if berapa > palingPanjang:
            palingPanjang = berapa

    print(palingPanjang)


def main():
    # t = int(input())
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()