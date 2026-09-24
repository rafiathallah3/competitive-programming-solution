/*
Author: rafia
Problem: Minus Two
Link: https://codeforces.com/contest/2259/problem/B
Created: 2026-09-05 23:34:07
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
#define endl '\n'
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
const int dx[4] = {1, 0, -1, 0}, dy[4] = {0, 1, 0, -1};
const int d8x[8] = {-1, -1, -1, 0, 0, 1, 1, 1},
          d8y[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

// Min / Max helpers
template <typename T> bool chmin(T &a, const T &b) {
    if (b < a) {
        a = b;
        return true;
    }
    return false;
}
template <typename T> bool chmax(T &a, const T &b) {
    if (a < b) {
        a = b;
        return true;
    }
    return false;
}

// Debugging
#ifdef LOCAL
#define debug(x) cerr << #x << " = " << (x) << '\n'
#else
#define debug(...)
#endif

void solve() {
    ll n;
    cin >> n;

    int count_odd = 0;
    int count_mod4_0 = 0;
    int count_mod4_2 = 0;
    rep(i, 0, n) {
        ll x;
        cin >> x;

        if (x % 2 != 0) {
            count_odd++;
        } else if (x % 4 == 0) {
            count_mod4_0++;
        } else {
            count_mod4_2++;
        }
    }

    int palingBesar = max({count_odd, count_mod4_0, count_mod4_2});
    cout << palingBesar << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; ++t) {
        // cout << "Case #" << t << ": ";
        solve();
    }

    return 0;
}