"""
Program to create competitive programming files with templates
"""

import os
import sys
import argparse
from datetime import datetime


def create_python_template(author, problem_name, link, date):
    """Creates a Python competitive programming template"""
    template = f'''"""
Author: {author}
Problem: {problem_name}
Link: {link}
Created: {date}
"""

import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
from math import gcd, sqrt, ceil, floor, factorial

sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().strip()

def ii(): return int(input()) 
def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))

def solve():
    pass

def main():
    # t = int(input())
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
'''
    return template


def create_cpp_template(author, problem_name, link, date):
    """Creates a C++ competitive programming template"""
    template = f"""/*
Author: {author}
Problem: {problem_name}
Link: {link}
Created: {date}
*/

#include <bits/stdc++.h>
using namespace std;

// Type definitions
using ll = long long;
using ull = unsigned long long;
using ld = long double;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vi = vector<int>;
using vll = vector<ll>;
using vvi = vector<vector<int>>;
using vvll = vector<vector<ll>>;
using vpii = vector<pii>;
using vpll = vector<pll>;

// Shortcuts & Macros
#define endl '\\n'
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define fi first
#define se second
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define sz(x) static_cast<int>((x).size())
#define rep(i, a, b) for (int i = (a); i < (b); ++i)
#define per(i, a, b) for (int i = (b) - 1; i >= (a); --i)
#define forn(i, n) rep(i, 0, n)
#define forr(i, n) per(i, 0, n)

// Constants
const int INF = 1e9 + 7;
const ll LINF = 1e18 + 7;
const int MOD = 1e9 + 7; // 998244353
const ld PI = acos(-1.0);
const ld EPS = 1e-9;
const int dx[4] = {{1, 0, -1, 0}}, dy[4] = {{0, 1, 0, -1}};
const int d8x[8] = {{-1, -1, -1, 0, 0, 1, 1, 1}}, d8y[8] = {{-1, 0, 1, -1, 1, -1, 0, 1}};

// Min / Max helpers
template <typename T> bool chmin(T &a, const T &b) {{ if (b < a) {{ a = b; return true; }} return false; }}
template <typename T> bool chmax(T &a, const T &b) {{ if (a < b) {{ a = b; return true; }} return false; }}

// Debugging
#ifdef LOCAL
#define debug(x) cerr << #x << " = " << (x) << '\\n'
#else
#define debug(...)
#endif

void solve() {{
    
}}

int main() {{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int tc = 1;
    // cin >> tc;
    for (int t = 1; t <= tc; ++t) {{
        // cout << "Case #" << t << ": ";
        solve();
    }}
    
    return 0;
}}
"""
    return template


def get_valid_filename(name):
    """Converts problem name to a valid filename"""
    # Replace spaces and special characters with underscores
    filename = name.replace(" ", "_")
    filename = "".join(c for c in filename if c.isalnum() or c in "_-.")
    return filename


def main():
    parser = argparse.ArgumentParser(
        description="Create competitive programming files with templates",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python BuatFile.py --python "Two Sum" "https://leetcode.com/problems/two-sum/"
  python BuatFile.py --cpp "Array Problems" "https://codeforces.com/problemset/problem/1/A"
  python BuatFile.py --python "Test" "link" --author "John Doe"
        """,
    )

    # Language selection (mutually exclusive)
    language_group = parser.add_mutually_exclusive_group(required=True)
    language_group.add_argument(
        "--python",
        "--py",
        action="store_const",
        const="python",
        dest="language",
        help="Create a Python file",
    )
    language_group.add_argument(
        "--cpp",
        "--c++",
        action="store_const",
        const="cpp",
        dest="language",
        help="Create a C++ file",
    )

    # Required arguments
    parser.add_argument("problem_name", type=str, help="Name of the problem")
    parser.add_argument("link", type=str, help="Link to the problem")

    # Optional arguments
    parser.add_argument(
        "--author",
        "-a",
        type=str,
        default=os.getenv("USER") or os.getenv("USERNAME") or "rafia",
        help='Author name (default: system username or "Unknown")',
    )
    parser.add_argument(
        "--overwrite",
        "-f",
        action="store_true",
        help="Overwrite existing file without asking",
    )

    args = parser.parse_args()

    # Get creation date
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Determine file extension
    extension = ".py" if args.language == "python" else ".cpp"

    # Generate filename
    filename = get_valid_filename(args.problem_name)
    if not filename:
        filename = "solution"

    filename = filename + extension

    # Check if file already exists
    if os.path.exists(filename) and not args.overwrite:
        response = (
            input(f"File '{filename}' already exists. Overwrite? (y/n): ")
            .strip()
            .lower()
        )
        if response != "y":
            print("Operation cancelled.")
            return

    # Generate template
    if args.language == "python":
        content = create_python_template(
            args.author, args.problem_name, args.link, date
        )
    else:
        content = create_cpp_template(args.author, args.problem_name, args.link, date)

    # Write file
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✓ Successfully created '{filename}'")
        print(f"  Author: {args.author}")
        print(f"  Problem: {args.problem_name}")
        print(f"  Date: {date}")
    except Exception as e:
        print(f"✗ Error creating file: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
