#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<string> arr(n);
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    int cost1 = 0, cost2 = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if ((i + j) % 2 == 0 && arr[i][j] != 'R')
                cost1 += 3;
            if ((i + j) % 2 == 1 && arr[i][j] != 'G')
                cost1 += 5;
            if ((i + j) % 2 == 0 && arr[i][j] != 'G')
                cost2 += 5;
            if ((i + j) % 2 == 1 && arr[i][j] != 'R')
                cost2 += 3;
        }
    }
    cout << min(cost1, cost2) << endl;
    return 0;
}