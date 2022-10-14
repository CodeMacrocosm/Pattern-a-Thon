#include<iostream>
using namespace std;

int main()
{
	int i, j, k, rows;
     
    cout << "Enter Diamond Star Pattern Row = ";
    cin >> rows;

    cout << "Diamond Star Pattern\n"; 

    for(i = 1; i <= rows; i++)
    {
    	for(j = 1; j <= rows - i; j++)
		{
            cout << " ";
        }
        for(k = 1; k <= i * 2 - 1; k++)
        {
            cout << "*";
        }
        cout << "\n";
    }	

    for(i = rows - 1; i > 0; i--)
    {
    	for(j = 1; j <= rows - i; j++)
		{
            cout << " ";
        }
        for(k = 1; k <= i * 2 - 1; k++)
        {
            cout << "*";
        }
        cout << "\n";
    }
	
 	return 0;
}
