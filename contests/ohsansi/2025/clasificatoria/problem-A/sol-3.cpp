#include <iostream>

using namespace std;

int main() {

    int n;
    cin >> n;

    int ans = 0;

    for (int i = 1; i <= n; i++) {
        if (i % 2 == 1) {
            ans++;
        }
    }

    cout << ans << endl;

    return 0;
}