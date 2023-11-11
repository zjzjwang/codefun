#include <bits/stdc++.h>
using namespace std;

int n, x, y;
int dp[5005][55];
int a[105], b[105];

int main() {
#ifdef INPUT
  freopen("in.txt", "r", stdin);
#endif

  cin >> n >> x >> y;
  for (int i = 1; i <= n; ++i) {
    cin >> a[i] >> b[i];
  }

  // memset(dp, 0, sizeof(dp)); // 默认初始化为0
  // dp[i][j][k]: 前i件商品，花费不超过j元，使用k个优惠卷 最多能买几件
  int cnt = 0, cost = 0;
  for (int i = 1; i <= n; ++i) {
    for (int j = x; j >= 0; --j) {
      for (int k = 0; k <= y; ++k) {
        if (j >= a[i]) {
          dp[j][k] = max(dp[j][k], dp[j - a[i]][k] + 1);
        }
        if (j >= b[i] && k > 0) {
          dp[j][k] = max(dp[j][k], dp[j - b[i]][k - 1] + 1);
        }

        if (dp[j][k] > cnt) {
          cnt = dp[j][k];
          cost = j;
        } else if (dp[j][k] == cnt) {
          cost = min(cost, j);
        }
      }
    }
  }
  cout << cnt << " " << cost << endl;
  return 0;
}
