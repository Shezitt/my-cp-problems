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
    }

    int last = -1;
    for (int i = 0; i < n; i++) {
        if (a[i] != last) {
            res.push_back(a[i]);
            last = a[i];
        }
    }

    for (int i = 0; i < res.size(); i++) {
        cout << res[i] << " ";
    }
    cout << endl;

    return 0;
}