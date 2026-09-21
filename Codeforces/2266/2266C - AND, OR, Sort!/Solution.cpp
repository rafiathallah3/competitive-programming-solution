/*
Author: rafia
Problem: AND, OR, Sort!
Link: https://codeforces.com/contest/2266/problem/C
Created: 2026-09-21 22:38:37
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
    string s;
    cin >> s;

    // Cek apakah sudah terurut
    bool sudah_sorted = true;
    for (int i = 0; i < n - 1; i++) {
        if (s[i] > s[i + 1]) {
            sudah_sorted = false;
            break;
        }
    }
    if (sudah_sorted) {
        cout << 0 << endl;
        return;
    }

    // Karakter pertama s[0] tidak pernah bisa diubah!
    // Jika s[0] == '1', satu-satunya string terurut yang mungkin adalah "111...1"
    if (s[0] == '1') {
        int jumlah0 = 0;
        for (char c : s) {
            if (c == '0') jumlah0++;
        }
        cout << jumlah0 << endl;
        return;
    }

    // Jika s[0] == '0':
    // Cari posisi '1' pertama (0-indexed)
    int first_one = -1;
    for (int i = 0; i < n; i++) {
        if (s[i] == '1') {
            first_one = i;
            break;
        }
    }

    // Prefix sum jumlah '1'
    // pref1[i] = jumlah '1' pada prefix s[0 ... i - 1]
    vi pref1(n + 1, 0);
    for (int i = 0; i < n; i++) {
        pref1[i + 1] = pref1[i] + (s[i] == '1');
    }

    // String terurut berbentuk 0...0 1...1 (k buah 0 diikuti n-k buah 1).
    // Karena semua posisi sebelum first_one awalnya bernilai 0,
    // posisi-posisi tersebut tidak akan pernah bisa menjadi 1.
    // Oleh karena itu, k (banyaknya '0') harus bernilai antara first_one sampai n.
    int ans = n;
    for (int k = first_one; k <= n; k++) {
        // Jumlah '1' di s[0 ... k-1] yang harus diubah menjadi '0'
        int cost0 = pref1[k];
        // Jumlah '0' di s[k ... n-1] yang harus diubah menjadi '1'
        int cost1 = (n - k) - (pref1[n] - pref1[k]);
        ans = min(ans, cost0 + cost1);
    }

    cout << ans << endl;
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