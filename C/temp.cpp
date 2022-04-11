#include <iostream>
using namespace std;

long long arr[100005];
int main()
{
  int k, n;
  cin >> k >> n;
  long long sum = 0;
  arr[0] = 0;
  for (int i = 1; i <= n; i++)
  {
    cin >> arr[i];
    sum += arr[i];
    arr[i] += arr[i - 1];
  }
  int p = n - k;
  long long maxi = 0;
  for (int i = 1; i <= n - p + 1; i++)
  {
    long long here = arr[i + p - 1] - arr[i - 1];
    maxi = max(maxi, sum - here);
  }
  cout << maxi;
}