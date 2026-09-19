# [2065A] Skibidus and Amog'u

**Platform:** CODEFORCES  
**Problem URL:** [https://codeforces.com/problemset/problem/2065/A?adcd1e=caf4ft0r28b5km&csrf_token=98e9823ab9f9e7ae55f10f5a1756f4d3&__cf_chl_tk=qoLxCA6aUFzR7IL2n0Oqw2XQoQ.3PxoYCn3p705Cx4Y-1789831513-1.0.1.1-fz7nT8Q9p3xISvIWUSe6nD3cBSTDn.6n0NVL9qA3LMQ](https://codeforces.com/problemset/problem/2065/A?adcd1e=caf4ft0r28b5km&csrf_token=98e9823ab9f9e7ae55f10f5a1756f4d3&__cf_chl_tk=qoLxCA6aUFzR7IL2n0Oqw2XQoQ.3PxoYCn3p705Cx4Y-1789831513-1.0.1.1-fz7nT8Q9p3xISvIWUSe6nD3cBSTDn.6n0NVL9qA3LMQ)  
**Rating / Difficulty:** 800  
**Tags:** `brute force`, `constructive algorithms`, `greedy`, `implementation`, `strings`  
**Time Limit:** 1 second  
**Memory Limit:** 256 megabytes  

## Submission Details

- **Status:** Accepted
- **Language:** C++23 (GCC 14-64, msys2)
- **Execution Time:** 0 ms
- **Memory Used:** 0 KB
- **Submitted At:** Sat, 19 Sep 2026 15:25:17 GMT

## Problem Statement

A. Skibidus and Amog'utime limit per test1 secondmemory limit per test256 megabytesinputstandard inputoutputstandard output
    
    Sync to GitHub
  Found submission #391244715! Locating source code...
Skibidus lands on a foreign planet, where the local Amog tribe speaks the Amog'u language. In Amog'u, there are two forms of nouns, which are singular and plural.

Given that the root of the noun is transcribed as SS, the two forms are transcribed as:

 -  Singular: SS ++ "us" 
-  Plural: SS ++ "i" 

Here, ++ denotes string concatenation. For example, abc ++ def == abcdef.

For example, when SS is transcribed as "amog", then the singular form is transcribed as "amogus", and the plural form is transcribed as "amogi". Do note that Amog'u nouns can have an empty root — in specific, "us" is the singular form of "i" (which, on an unrelated note, means "imposter" and "imposters" respectively).

Given a transcribed Amog'u noun in singular form, please convert it to the transcription of the corresponding plural noun.
Input
Each test contains multiple test cases. The first line contains the number of test cases tt (1≤t≤1001≤t≤100). The description of the test cases follows. 

The only line of each test case contains a string WW, which is a transcribed Amog'u noun in singular form. It is guaranteed that WW consists of only lowercase English letters, has a length of at most 1010, and ends with "us".
Output
For each test case, output the transcription of the corresponding plural noun on a separate line.
ExampleInputCopy
```
9ussusfunguscactussussusamoguschungusntarsusskibidus
```
OutputCopy
```
i
si
fungi
cacti
sussi
amogi
chungi
ntarsi
skibidi

```

---
*Generated automatically with [CPBase](https://github.com/)*