/*
https://codefun2000.com/p/P1077
meituan 2023.3.11-第一题-字符串修改

2023年10月30日 16点15分
*/

#include <bits/stdc++.h>
using namespace std;

int solve(string &s) {
  int n = s.size();
  int res = 0;
  for (int i = 1; i < n; ++i) {
    if (s[i] == s[i - 1]) {
      s[i] = '*';
      res += 1;
    }
  }
  return res;
}

int main(int argc, char const *argv[]) {
  string s;
  cin >> s;

  auto res = solve(s);
  cout << res << endl;

  return 0;
}
