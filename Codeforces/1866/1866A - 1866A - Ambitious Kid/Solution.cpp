/*
Author: Rafi
Problem: Ambitious Kid
Link: https://codeforces.com/problemset/problem/1866/A
Created: 2026-08-23 23:50:03
*/

#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define ll long long
#define vi vector<int>
#define vll vector<long long>
#define vvi vector<vector<int>>
#define pii pair<int, int>
#define pll pair<long long, long long>
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define rep(i, n) for (int i = 0; i < n; i++)
#define REP(i, k, n) for (int i = k; i < n; i++)

void solve() {
    int n;
    cin >> n;
    vi l(n, 0);
    rep(i, n) {
        cin >> l[i];
        l[i] = abs(l[i]);
    }

    bool apakahAda0 = find(all(l), 0) != l.end();
    if (apakahAda0) {
        cout << 0 << endl;
        return;
    }

    int palingKecil = *min_element(all(l));
    cout << abs(palingKecil) << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // int t;
    // cin >> t;
    // while (t--) {
    //     solve();
    // }

    solve();

    return 0;
}