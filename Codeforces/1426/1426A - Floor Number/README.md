# [1426A] Floor Number

**Platform:** CODEFORCES  
**Problem URL:** [https://codeforces.com/problemset/problem/1426/A](https://codeforces.com/problemset/problem/1426/A)  
**Rating / Difficulty:** 800  
**Tags:** `implementation`, `math`  
**Time Limit:** 1 second  
**Memory Limit:** 256 megabytes  

## Submission Details

- **Status:** Accepted
- **Language:** C++23 (GCC 14-64, msys2)
- **Execution Time:** 31 ms
- **Memory Used:** 0 KB
- **Submitted At:** Sat, 19 Sep 2026 17:25:22 GMT

## Problem Statement

Vasya goes to visit his classmate Petya. Vasya knows that Petya's apartment number is $n$$n$. 

There is only one entrance in Petya's house and the distribution of apartments is the following: the first floor contains $2$$2$ apartments, every other floor contains $x$$x$ apartments each. Apartments are numbered starting from one, from the first floor. I.e. apartments on the first floor have numbers $1$$1$ and $2$$2$, apartments on the second floor have numbers from $3$$3$ to $(x+2)$$(x + 2)$, apartments on the third floor have numbers from $(x+3)$$(x + 3)$ to $(2⋅x+2)$$(2 \cdot x + 2)$, and so on.

Your task is to find the number of floor on which Petya lives. Assume that the house is always high enough to fit at least $n$$n$ apartments.

You have to answer $t$$t$ independent test cases.

### Input

The first line of the input contains one integer $t$$t$ ($1≤t≤1000$$1 \le t \le 1000$) — the number of test cases. Then $t$$t$ test cases follow.

The only line of the test case contains two integers $n$$n$ and $x$$x$ ($1≤n,x≤1000$$1 \le n, x \le 1000$) — the number of Petya's apartment and the number of apartments on each floor of the house except the first one (there are two apartments on the first floor).

### Output

For each test case, print the answer: the number of floor on which Petya lives.

## Example

**Input**
```text
4
7 3
1 5
22 5
987 13
```

**Output**
```text
3
1
5
77
```


## Note

Consider the first test case of the example: the first floor contains apartments with numbers $1$$1$ and $2$$2$, the second one contains apartments with numbers $3$$3$, $4$$4$ and $5$$5$, the third one contains apartments with numbers $6$$6$, $7$$7$ and $8$$8$. Therefore, Petya lives on the third floor.

In the second test case of the example, Petya lives in the apartment $1$$1$ which is on the first floor.

---
*Generated automatically with [CPBase](https://github.com/)*