#include <iostream>
#include <vector>

using namespace std;

int main() {

    int n, k;
    cin >> n >> k;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int ans = 0;
    for (int i = 0; i < k; i++) {
        ans += a[i];
    }

    cout << ans << endl;

    return 0;
}