#include <iostream>
#include <vector>

using namespace std;

int main() {

    int n;
    cin >> n;
    vector<int> a(n);
    vector<int> res;

    for (int i = 0; i < n; i++) {
        cin >> a[i];
        cout << a[i] << ' ';
    }

    return 0;
}