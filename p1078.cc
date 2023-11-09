#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 10;
int n, l[N], r[N];

int main() {
  cin >> n;
  for (int i = 0; i < n; ++i)
    cin >> l[i];
  for (int i = 0; i < n; ++i)
    cin >> r[i];

  map<int, int> mp;

  for (int i = 0; i < n; ++i) {
    int a = l[i], b = r[i];
    mp[a]++;
    mp[b + 1]--;
  }
  unordered_map<int, int> cnts;
  int sum = 0, pre = *min_element(l, l + n);
  for (auto &[k, v] : mp) {
    cnts[sum] += k - pre;
    sum += v;
    pre = k;
  }

  int x = 0, y = 0;
  for (auto &[k, v] : cnts) {
    if (k > x) {
      x = k;
      y = v;
    }
  }
  cout << x << " " << y << endl;
  return 0;
}
