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

    long long ans = 0;
    for (int i = n - k; i < n; i++) {
        ans += a[i];
    }

    cout << ans << endl;

    return 0;
}