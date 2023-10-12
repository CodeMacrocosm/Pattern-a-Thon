#include<iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        for(int s = 0; s < n - i - 1; s++){
            cout << " ";
        }
        for(int j = 0; j < i*2 + 1; j++){
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}