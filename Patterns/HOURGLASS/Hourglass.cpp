#include <iostream>
using namespace std;
int main()
{
  int n;
  cin >> n;
  int space = 0;
  int stars = n;
  for (int i = 1; i <= n; i++)
  {
    for (int j = 1; j <= space; j++)
    {
      cout << "\t";
    }
    for (int j = 1; j <= stars; j++)
    {
      if (i > 1 && i <= n / 2 && j > 1 && j < stars)
      {
        cout << "\t";
      }
      else
      {
        cout << "*\t";
      }
    }

    if (i <= n / 2)
    {
      stars -= 2;
      space++;
    }
    else
    {
      stars += 2;
      space--;
    }
    cout << endl;
  }
  return 0;
}
