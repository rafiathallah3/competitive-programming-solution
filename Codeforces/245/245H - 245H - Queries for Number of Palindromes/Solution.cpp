#include<bits/stdc++.h>
using namespace std;

vector<vector<bool>> dx(5005,vector<bool>(5005));
vector<vector<int>> dp(5005,vector<int>(5005));
void xuantuyen(int n,string s){
    for(int i = n;i>0;i--){
        for(int j = i;j<=n;j++){
            if(i == j){
                dp[i][j] = 1;
                dx[i][j] = 1;
            }
            else if(j - i == 1){
                dx[i][j] = (s[i] == s[j]);
                dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1] + dx[i][j];
            }
            else{
                dx[i][j] = (s[i] == s[j]) && dx[i+1][j-1];
                dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1] + dx[i][j];
            }
        }
    }
}

int main(){
    //freopen("stdin","r",stdin);
    //freopen("stdout","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    int q;
    cin >> s;
    s = " " + s;
    cin >> q;
    int n = s.size() - 1;
    xuantuyen(n,s);
    long long l,r;
    while(q--){
        cin >> l >> r;
        cout << dp[l][r] << '\n';
    }

}