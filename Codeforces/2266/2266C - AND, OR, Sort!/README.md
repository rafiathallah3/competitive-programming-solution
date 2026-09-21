# [2266C] AND, OR, Sort!

**Platform:** CODEFORCES  
**Problem URL:** [https://codeforces.com/contest/2266/problem/C](https://codeforces.com/contest/2266/problem/C)  
**Time Limit:** 2 seconds  
**Memory Limit:** 256 megabytes  

## Submission Details

- **Status:** Accepted
- **Language:** C++23 (GCC 14-64, msys2)
- **Execution Time:** 46 ms
- **Memory Used:** 0 KB
- **Submitted At:** Mon, 21 Sep 2026 16:13:31 GMT

## Problem Statement

You are given a **binary string**$∗$$^{\text{∗}}$ $s$$s$ of length $n$$n$.

You may perform the following operation any number of times (possibly zero):

 -  choose an integer $i$$i$ ($1≤i≤n$$1 \le i \le n$), and replace $si$$s_i$ with either the bitwise AND or the bitwise OR of $s1,s2,…,si$$s_1, s_2, \ldots, s_i$. 

Note that the bitwise AND or bitwise OR of a single element is equal to the element itself.

Your goal is to make $s$$s$ sorted in non-decreasing order$†$$^{\text{†}}$.

Find the minimum number of operations required to sort $s$$s$ in non-decreasing order.

$∗$$^{\text{∗}}$A binary string only contains characters $0$$\texttt{0}$ and $1$$\texttt{1}$.

$†$$^{\text{†}}$If $s$$s$ is in non-decreasing order, then $s1≤s2≤…≤sn$$s_1 \leq s_2 \leq \ldots \leq s_n$.

### Input

The first line contains a single integer $t$$t$ ($1≤t≤104$$1 \le t \le 10^4$) — the number of test cases.

The first line of each test case contains a single integer $n$$n$ ($2≤n≤2⋅105$$2 \le n \le 2 \cdot 10^5$) — the length of the binary string $s$$s$.

The second line of each test case contains the binary string $s$$s$ of length $n$$n$. Each character of $s$$s$ is either `0` or `1`.

It is guaranteed that the sum of $n$$n$ over all test cases does not exceed $2⋅105$$2 \cdot 10^5$.

### Output

For each test case, print a single integer — the minimum number of operations required to sort $s$$s$ in non-decreasing order.

## Example

**Input**
```text
6
4
0011
4
1000
5
01000
8
01001101
7
0101010
7
0111101
```

**Output**
```text
0
3
1
2
3
1
```


## Note

In the first test case, the string is already sorted, so no operations are required.

In the second test case, we can use bitwise OR to change the last three characters to `1`, obtaining `1111` in $3$$3$ operations.

---
*Generated automatically with [CPBase](https://github.com/)*