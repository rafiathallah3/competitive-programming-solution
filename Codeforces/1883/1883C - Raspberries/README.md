# [1883C] Raspberries

**Platform:** CODEFORCES  
**Problem URL:** [https://codeforces.com/problemset/problem/1883/C](https://codeforces.com/problemset/problem/1883/C)  
**Rating / Difficulty:** 1000  
**Tags:** `dp`, `math`  
**Time Limit:** 2 seconds  
**Memory Limit:** 256 megabytes  

## Submission Details

- **Status:** Accepted
- **Language:** C++23 (GCC 14-64, msys2)
- **Execution Time:** 46 ms
- **Memory Used:** 0 KB
- **Submitted At:** Tue, 22 Sep 2026 17:16:41 GMT

## Problem Statement

You are given an array of integers $a1,a2,…,an$$a_1, a_2, \ldots, a_n$ and a number $k$$k$ ($2≤k≤5$$2 \leq k \leq 5$). In one operation, you can do the following:

-  Choose an index $1≤i≤n$$1 \leq i \leq n$,
-  Set $ai=ai+1$$a_i = a_i + 1$.

Find the minimum number of operations needed to make the product of all the numbers in the array $a1⋅a2⋅…⋅an$$a_1 \cdot a_2 \cdot \ldots \cdot a_n$ divisible by $k$$k$.

### Input

Each test consists of multiple test cases. The first line contains a single integer $t$$t$ ($1≤t≤104$$1 \leq t \leq 10^4$) — the number of test cases. Then follows the description of the test cases.

The first line of each test case contains two integers $n$$n$ and $k$$k$ ($2≤n≤105$$2 \leq n \leq 10^5$, $2≤k≤5$$2 \leq k \leq 5$) — the size of the array $a$$a$ and the number $k$$k$.

The second line of each test case contains $n$$n$ integers $a1,a2,…,an$$a_1, a_2, \ldots, a_n$ ($1≤ai≤10$$1 \leq a_i \leq 10$).

It is guaranteed that the sum of $n$$n$ over all test cases does not exceed $2⋅105$$2 \cdot 10^5$.

### Output

For each test case, output the minimum number of operations needed to make the product of all the numbers in the array divisible by $k$$k$.

## Example

**Input**
```text
15
2 5
7 3
3 3
7 4 1
5 2
9 7 7 3 9
5 5
5 4 1 2 3
7 4
9 5 1 5 9 5 1
3 4
6 3 6
3 4
6 1 5
3 4
1 5 9
4 4
1 4 1 1
3 4
3 5 3
4 5
8 9 9 3
2 5
1 6
2 5
10 10
4 5
1 6 1 1
2 5
7 7
```

**Output**
```text
2
2
1
0
2
0
1
2
0
1
1
4
0
4
3
```


## Note

In the first test case, we need to choose the index $i=2$$i = 2$ twice. After that, the array will be $a=[7,5]$$a = [7, 5]$. The product of all the numbers in the array is $35$$35$.

In the fourth test case, the product of the numbers in the array is $120$$120$, which is already divisible by $5$$5$, so no operations are needed.

In the eighth test case, we can perform two operations by choosing $i=2$$i = 2$ and $i=3$$i = 3$ in any order. After that, the array will be $a=[1,6,10]$$a = [1, 6, 10]$. The product of the numbers in the array is $60$$60$.

---
*Generated automatically with [CPBase](https://github.com/)*