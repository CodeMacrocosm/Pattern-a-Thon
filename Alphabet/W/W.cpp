#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++)
  {
    for (int j = 1; j <= n; j++)
    {
      if (j == 1 || j == n)
      {
        cout << "*	";
      }
      else if (i > n / 2 && (i == j || i + j == n + 1))
      {
        cout << "*	";
      }
      else
      {
        cout << "	";
      }
    }
    cout << endl;
  }
}
