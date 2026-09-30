"""
Author: Rafi
Problem: United We Stand
Link: https://codeforces.com/problemset/problem/1859/A
Created: 2026-08-09 22:25:57
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

    l.sort()
    if len(set(l)) <= 1:
        print(-1)
        return

    a = []
    b = []
    palingKecil = l[0]
    for i in range(n):
        if l[i] == palingKecil:
            a.append(l[i])
            continue
        b.append(l[i])

    print(len(a), len(b))
    print(" ".join(str(i) for i in a))
    print(" ".join(str(i) for i in b))


def main():
    t = int(input())
    # t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()