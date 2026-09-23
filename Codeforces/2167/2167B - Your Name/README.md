# [2167B] Your Name

**Platform:** CODEFORCES  
**Problem URL:** [https://codeforces.com/problemset/problem/2167/B](https://codeforces.com/problemset/problem/2167/B)  
**Rating / Difficulty:** 800  
**Tags:** `sortings`, `strings`  
**Time Limit:** 1 second  
**Memory Limit:** 256 megabytes  

## Submission Details

- **Status:** Accepted
- **Language:** C++23 (GCC 14-64, msys2)
- **Execution Time:** 31 ms
- **Memory Used:** 0 KB
- **Submitted At:** Wed, 23 Sep 2026 17:53:27 GMT

## Problem Statement

khba is writing his girlfriend's name. He has $n$$n$ cubes, each with one lowercase Latin letter written on it. They are arranged in a row, forming a string $s$$s$. His girlfriend's name is also a string $t$$t$, consisting of $n$$n$ lowercase Latin letters.

To prove his love, he must check whether it is possible to rearrange the letters of string $s$$s$ so that it becomes her name $t$$t$.

### Input

The first line contains an integer $q$$q$ ($1≤q≤1000$$1 \le q \le 1000$) — the number of test cases.

The first line of each test case contains an integer $n$$n$ ($1≤n≤20$$1 \le n \le 20$).

The second line of each test case contains two distinct strings $s$$s$ and $t$$t$, each consisting of $n$$n$ lowercase Latin letters.

### Output

For each test case, output "`YES`" if the letters of $s$$s$ can be arranged to form $t$$t$; otherwise, output "`NO`". 

You can output the answer in any case (upper or lower). For example, the strings "`yEs`", "`yes`", "`Yes`" and "`YES`" will be recognized as positive responses.

## Example

**Input**
```text
5
7
humitsa mitsuha
4
orhi hori
6
aakima makima
6
nezuqo nezuko
6
misaka mikasa
```

**Output**
```text
YES
YES
NO
NO
YES
```


## Note

In the first example, the initial string is "`humitsa`", and the following operations can be performed: 

 -  swap the first and third characters, resulting in "`muhitsa`" 
-  swap the second and fourth characters, resulting in "`mihutsa`" 
-  swap the third and fifth characters, resulting in "`mithusa`" 
-  swap the fourth and sixth characters, resulting in "`mitsuha`" 

In the second example, the initial string is "`orhi`", and the following operations can be performed: 

 -  swap the second and third characters, resulting in "`ohri`" 
-  swap the first and second characters, resulting in "`hori`"

---
*Generated automatically with [CPBase](https://github.com/)*