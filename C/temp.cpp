#include <iostream>
using namespace std;

#define ull unsigned long long int

bool conditionSort(const pair<ull, ull> &x, const pair<ull, ull> &y)
{
  if (x.second == y.second)
    return (x.first < y.first);
  else
    return (x.second > y.second);
}

int main()
{
  
  cout << "Hello";
}
