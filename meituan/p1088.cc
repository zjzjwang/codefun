#include <bits/stdc++.h>
using namespace std;

int solve(vector<int> &colors, int k) {
  int ans = 0;
  int n = colors.size();
  unordered_map<int, int> cnt;

  int left = 0, right = 0;
  while (right < n) {
    int cr = colors[right++];
    if (cnt.find(cr) != cnt.end()) {
      cnt[cr]++;
    } else {
      cnt[cr] = 1;
    }
    while (cnt.size() > k) {
      int cl = colors[left++];
      cnt[cl] -= 1;
      if (cnt[cl] == 0) {
        cnt.erase(cl);
      }
    }
    ans = max(ans, right - left);
  }
  return ans;
}

int main(int argc, char *argv[]) {
  int n, k;
  cin >> n >> k;
  vector<int> colors(n);
  for (int i = 0; i < n; i++) {
    cin >> colors[i];
  }

  auto res = solve(colors, k);
  cout << res << endl;
  return 0;
}
