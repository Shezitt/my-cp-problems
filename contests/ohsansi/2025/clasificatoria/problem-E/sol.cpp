#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<int> dp(n+1, 1e9+5);
    dp[0] = 0;

    int ans = 1;

    for (int i = 0; i < n; ++i) {
        int x = a[i];
        int j = upper_bound(dp.begin(), dp.end(), x) - dp.begin();
        if (dp[j-1] < x) {
            dp[j] = x;
            ans = max(ans, j);
        }
    }

    cout << ans << endl;

    return 0;
}