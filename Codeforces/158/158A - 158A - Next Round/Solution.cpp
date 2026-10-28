#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, k;
    cin >> n >> k;
    vector<int> Izzan(n);
    for (int &Auzi : Izzan) {
        cin >> Auzi;
    }

    int Mulyana = 0;
    for (int putra = 0; putra < n; putra++) {
        if (Izzan[putra] >= Izzan[k - 1] && Izzan[putra] > 0) {
            Mulyana++;
        }
    }

    cout << Mulyana;

    return 0;
}