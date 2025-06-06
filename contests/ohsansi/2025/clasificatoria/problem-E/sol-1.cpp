#include <vector>
#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  for (int &i : a) {
    cin >> i;
  }
  cout << n << endl;
}