#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e5 + 17;
int n, d[maxn], p[maxn];
bool mark[maxn];
int main()
{
  ios::sync_with_stdio(0), cin.tie(0);
  int t;
  cin >> t;
  while (t--)
  {
    cin >> n;
    for (int i = 0; i < n; i++)
      cin >> p[i], p[i]--;
    fill(d + 1, d + n, n);
    memset(mark, 0, sizeof mark);
    queue<int> q({0});
    while (q.size())
    {
      int i = q.front();
      q.pop();
      if (mark[i])
        continue;
      mark[i] = 1;
      vector<int> self({i});
      while (p[self.back()] != i)
      {
        self.push_back(p[self.back()]);
        d[self.back()] = d[i];
        mark[self.back()] = 1;
      }
      auto add = [&](int j)
      {
        if (d[j] <= d[i] + 1)
          return;
        d[j] = d[i] + 1;
        q.push(j);
      };
      for (auto i : self)
      {
        if (i)
          add(i - 1);
        if (i < n - 1)
          add(i + 1);
      }
    }
    cout << d[n - 1] << '\n';
  }
}