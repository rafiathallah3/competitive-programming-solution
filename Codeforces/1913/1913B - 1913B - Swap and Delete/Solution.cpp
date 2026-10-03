/*
Author: Rafi
Problem: Swap and Delete
Link: https://codeforces.com/problemset/problem/1913/B
Created: 2026-08-24 00:13:52
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
    string s;
    cin >> s;

    int jumlah0 = count(all(s), '0');
    int jumlah1 = count(all(s), '1');

    int hasil = 0;
    rep(i, s.length()) {
        if (s[i] == '1') {
            if (jumlah0 <= 0) {
                hasil = s.length() - i;
                break;
            }

            jumlah0--;
            continue;
        }

        if (s[i] == '0') {
            if (jumlah1 <= 0) {
                hasil = s.length() - i;
                break;
            }

            jumlah1--;
            continue;
        }
    }

    cout << hasil << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }

    // solve();

    return 0;
}