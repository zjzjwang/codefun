#include <bits/stdc++.h>
using namespace std;


int main() {
  int n, x, y;
  cin >> n >> x >> y;

  vector<pair<int, int>> items(n);
  for (int i = 0; i < n; ++i) {
    cin >> items[i].first >> items[i].second;
  }

  sort(items.begin(), items.end(), [](const pair<int, int>& a, const pair<int, int>&b) {
    if (a.second == b.second) return a.first > b.first;
    return a.second < b.second;
  });

  vector<int> prices(n);
  for (int i = 0; i < n; ++i) {
    if (y > 0) {  // discounted price < original price
      if (items[i].first > items[i].second) --y;
      prices[i] = items[i].second;
    } else {
      prices[i] = items[i].first;
    }
  }
  sort(prices.begin(), prices.end());
  int cnt = 0, cost = 0;
  for (int i = 0; i < n && x >= prices[i]; i++) {
    ++cnt;
    cost += prices[i];
    x -= prices[i];
  }
  cout << cnt << " " << cost << endl;
  return 0;
}