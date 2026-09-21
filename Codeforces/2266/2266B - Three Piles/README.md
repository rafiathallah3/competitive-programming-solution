# [2266B] Three Piles

**Platform:** CODEFORCES  
**Problem URL:** [https://codeforces.com/contest/2266/problem/B](https://codeforces.com/contest/2266/problem/B)  
**Time Limit:** 1 second  
**Memory Limit:** 256 megabytes  

## Submission Details

- **Status:** Accepted
- **Language:** C++23 (GCC 14-64, msys2)
- **Execution Time:** 31 ms
- **Memory Used:** 0 KB
- **Submitted At:** Mon, 21 Sep 2026 15:23:55 GMT

## Problem Statement

Alice and Bob are playing a game with three piles of stones. Initially, Alice has $a$$a$ stones, Bob has $b$$b$ stones, and the third pile contains $c$$c$ stones.

Alice and Bob take turns, with Alice going first. On each turn, the current player may take any number of stones from the third pile, possibly zero, and add them to their own pile.

If both players take zero stones on two consecutive turns, the game ends.

Let $A$$A$ and $B$$B$ be the final numbers of stones Alice and Bob have, respectively. The score of the game is $|A−B|$$|A-B|$.

Alice wants to maximize the score, while Bob wants to minimize it. Assuming both players play optimally, find the final score.

### Input

The first line contains an integer $t$$t$ ($1≤t≤104$$1 \le t \le 10^4$) — the number of test cases.

Each test case contains three integers $a$$a$, $b$$b$, and $c$$c$ ($0≤a,b,c≤109$$0 \le a,b,c \le 10^9$) — the initial numbers of stones Alice has, Bob has, and the third pile has, respectively.

### Output

For each test case, output one integer — the final score if both players play optimally.

It is important to use a $64$$64$-bit integer type, such as `long long` in C++.

## Example

**Input**
```text
5
3 6 3
3 6 10
5 5 4
2 5 6
67676767 41414141 998244353
```

**Output**
```text
3
7
4
3
1024506979
```


## Note

In the first test case, Alice can choose to take $0$$0$ stones on her first turn. Bob can then also take $0$$0$ stones, so the game ends with piles of sizes $3$$3$ and $6$$6$. Therefore, the score can be $3$$3$. It can be shown that Alice cannot achieve a larger score, and Bob cannot achieve a smaller score.

In the second test case, Alice can take all $10$$10$ stones from the third pile on her first turn. The game then ends with piles of sizes $13$$13$ and $6$$6$, so the score is $7$$7$.

---
*Generated automatically with [CPBase](https://github.com/)*